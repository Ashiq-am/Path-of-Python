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
    'vgg16': [1, 11, 18, 25, 20],
    'vgg19': [1, 6, 11, 20, 29, 22]
}
from fastai.callback.hook import hook_outputs

def get_feats(arch: str, pretrained=True):
    "Retrieve features from the specified VGG architecture"
    feat_net, layers = _get_layers(arch, pretrained)
    hooks = hook_outputs(layers, detach=False)
    def _inner(x):
        feat_net(x)
        return hooks.stored
    return _inner

# Extract features from the style image
im_feats = get_feats('vgg19')(style_im)
