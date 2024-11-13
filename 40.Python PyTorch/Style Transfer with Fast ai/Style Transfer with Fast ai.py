# Ensure we have a P100 GPU
!nvidia-smi

# Check CUDA availability
if not torch.cuda.is_available():
    raise RuntimeError("No CUDA available, please use a GPU runtime.")

# Function to get VGG layers
def _get_layers(arch: str, pretrained=True):
    "Get the layers and arch for a VGG Model (16 and 19 are supported only)"
    feat_net = vgg19(pretrained=pretrained).cuda() if arch.find('9') > 1 else vgg16(pretrained=pretrained).cuda()
    config = _vgg_config.get(arch)
    features = feat_net.features.cuda().eval()
    for p in features.parameters(): p.requires_grad=False
    return feat_net, [features[i] for i in config]

# Configuration for VGG16 and VGG19
_vgg_config = {
    'vgg16' : [1, 11, 18, 25, 20],
    'vgg19' : [1, 6, 11, 20, 29, 22]
}

# Get features
def get_feats(arch: str, pretrained=True):
    "Get the features of an architecture"
    feat_net, layers = _get_layers(arch, pretrained)
    hooks = hook_outputs(layers, detach=False)
    def _inner(x):
        feat_net(x)
        return hooks.stored
    return _inner

# Define Gram matrix function
def gram(x: Tensor):
    "Transpose a tensor based on c,w,h"
    n, c, h, w = x.shape
    x = x.view(n, c, -1)
    return (x @ x.transpose(1, 2)) / (c * w * h)

# Define style loss function
def style_loss(inp: Tensor, out_feat: Tensor):
    "Calculate style loss, assumes we have im_grams"
    bs = inp[0].shape[0]
    loss = []
    for y, f in zip(*map(get_stl_fs, [im_grams, inp])):
        loss.append(F.mse_loss(y.repeat(bs, 1, 1), gram(f)))
    return 3e5 * sum(loss)

# Define FeatureLoss class
class FeatureLoss(Module):
    "Combines two losses and features into a usable loss function"
    def __init__(self, feats, style_loss, act_loss):
        store_attr(self, 'feats, style_loss, act_loss')
        self.reset_metrics()

    def forward(self, pred, targ):
        pred_feat, targ_feat = self.feats(pred), self.feats(targ)
        style_loss = self.style_loss(pred_feat, targ_feat)
        act_loss = self.act_loss(pred_feat, targ_feat)
        self._add_loss(style_loss, act_loss)
        return style_loss + act_loss

    def reset_metrics(self):
        self.metrics = dict(style=[], content=[])

    def _add_loss(self, style_loss, act_loss):
        self.metrics['style'].append(style_loss)
        self.metrics['content'].append(act_loss)

# Define activation loss function
def act_loss(inp: Tensor, targ: Tensor):
    "Calculate the MSE loss of the activation layers"
    return F.mse_loss(inp[-1], targ[-1])

# Initialize the loss function
loss_func = FeatureLoss(get_feats('vgg19'), style_loss, act_loss)

# Define the model architecture
class ReflectionLayer(Module):
    "A series of Reflection Padding followed by a ConvLayer"
    def __init__(self, in_channels, out_channels, ks=3, stride=2):
        reflection_padding = ks // 2
        self.reflection_pad = nn.ReflectionPad2d(reflection_padding)
        self.conv2d = nn.Conv2d(in_channels, out_channels, ks, stride)

    def forward(self, x):
        out = self.reflection_pad(x)
        out = self.conv2d(out)
        return out

class ResidualBlock(Module):
    "Two reflection layers and an added activation function with residual"
    def __init__(self, channels):
        self.conv1 = ReflectionLayer(channels, channels, ks=3, stride=1)
        self.in1 = nn.InstanceNorm2d(channels, affine=True)
        self.conv2 = ReflectionLayer(channels, channels, ks=3, stride=1)
        self.in2 = nn.InstanceNorm2d(channels, affine=True)
        self.relu = nn.ReLU()

    def forward(self, x):
        residual = x
        out = self.relu(self.in1(self.conv1(x)))
        out = self.in2(self.conv2(out))
        out = out + residual
        return out

class UpsampleConvLayer(Module):
    "Upsample with a ReflectionLayer"
    def __init__(self, in_channels, out_channels, ks=3, stride=1, upsample=None):
        self.upsample = upsample
        reflection_padding = ks // 2
        self.reflection_pad = nn.ReflectionPad2d(reflection_padding)
        self.conv2d = nn.Conv2d(in_channels, out_channels, ks, stride)

    def forward(self, x):
        x_in = x
        if self.upsample:
            x_in = torch.nn.functional.interpolate(x_in, mode='nearest', scale_factor=self.upsample)
        out = self.reflection_pad(x_in)
        out = self.conv2d(out)
        return out

class TransformerNet(Module):
    "A simple network for style transfer"
    def __init__(self):
        super().__init__()
        self.conv1 = ReflectionLayer(3, 32, ks=9, stride=1)
        self.in1 = nn.InstanceNorm2d(32, affine=True)
        self.res1 = ResidualBlock(32)
        self.res2 = ResidualBlock(32)
        self.upsample = UpsampleConvLayer(32, 3, upsample=2)

    def forward(self, x):
        x = self.in1(self.conv1(x))
        x = self.res1(x)
        x = self.res2(x)
        x = self.upsample(x)
        return x

# Load style image
url = 'https://static.greatbigcanvas.com/images/singlecanvas_thick_none/megan-aroon-duncanson/little-village-abstract-art-house-painting,1162125.jpg'
!wget {url} -O 'style.jpg'

# Preprocess the style image
def get_style_im(url):
    download_url(url, 'style.jpg')
    fn = 'style.jpg'
    dset = Datasets(fn, tfms=[PILImage.create])
    dl = dset.dataloaders(after_item=[ToTensor()], after_batch=[IntToFloatTensor(), Normalize.from_stats(*imagenet_stats)], bs=1)
    return dl.one_batch()[0]

style_im = get_style_im(url)
im_feats = get_feats('vgg19')(style_im)

# Compute Gram matrices for the style features
im_grams = [gram(f) for f in im_feats]

# Now let's display the result using the TransformerNet
model = TransformerNet().cuda()
res = model(style_im.unsqueeze(0).cuda())

# Display the resulting image
TensorImage(res[0].cpu()).show()
