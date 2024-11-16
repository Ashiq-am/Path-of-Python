# import numpy library as alias np
import numpy as np

# applying .apply(), inside which passing
# the lambda function. lambda function,
# counting the no of states in each region
# where are more than 1000 family_members.
fam_1000 = df.groupby(level=["region"])["family_members].apply(lambda x : np.sum(x>1000))"]

print(fam_1000)
