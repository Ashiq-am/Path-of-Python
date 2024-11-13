class ReflectionLayer(nn.Module):
    "Reflection padding followed by convolution"
    def __init__(self, in_channels, out_channels, ks=3, stride=1):
        super().__init__()
        reflection_padding = ks // 2
        self.reflection_pad = nn.ReflectionPad2d(reflection_padding)
        self.conv2d = nn.Conv2d(in_channels, out_channels, ks, stride)

    def forward(self, x):
        out = self.reflection_pad(x)
        out = self.conv2d(out)
        return out

class ResidualBlock(nn.Module):
    "Residual block with two reflection layers and instance normalization"
    def __init__(self, channels):
        super().__init__()
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

class UpsampleConvLayer(nn.Module):
    "Upsampling followed by reflection padding and convolution"
    def __init__(self, in_channels, out_channels, ks=3, stride=1, upsample=None):
        super().__init__()
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

class TransformerNet(nn.Module):
    "Transformer network for style transfer"
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
