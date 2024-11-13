model = TransformerNet().cuda()
res = model(style_im.unsqueeze(0).cuda())
