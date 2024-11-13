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
