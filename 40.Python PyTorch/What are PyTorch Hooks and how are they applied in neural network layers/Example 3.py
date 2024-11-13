feats = {}

def hook_func(module, input, output):
    feats['feat'] = output.detach()
