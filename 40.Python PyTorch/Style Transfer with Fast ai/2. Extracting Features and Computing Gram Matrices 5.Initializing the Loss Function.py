# Initialize the loss function
loss_func = FeatureLoss(get_feats('vgg19'), style_loss, act_loss)
