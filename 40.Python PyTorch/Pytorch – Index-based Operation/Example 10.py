e=torch.ones([4,4])
indices2=torch.LongTensor([[0,1],[0,1],[2,1]])
value2=torch.zeros(indices2.shape[0])

e.index_put_(tuple(indices2.t()),value2,accumulate=True)
