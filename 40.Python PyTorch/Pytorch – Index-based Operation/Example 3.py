import torch

y=torch.ones(5,5)

index2=torch.tensor([0,1,1,1,2])
ten=torch.randn(1,5)
print("Indexed Matrix:\n",y.index_add(1,index2,ten))
print ("Printing Indexed Matrix again:\n",y)
