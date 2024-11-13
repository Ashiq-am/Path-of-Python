# Define style loss function
def style_loss(inp: Tensor, out_feat: Tensor):
    "Calculate style loss by comparing Gram matrices"
    bs = inp[0].shape[0]
    loss = []
    for y, f in zip(*map(get_stl_fs, [im_grams, inp])):
        loss.append(F.mse_loss(y.repeat(bs, 1, 1), gram(f)))
    return 3e5 * sum(loss)
