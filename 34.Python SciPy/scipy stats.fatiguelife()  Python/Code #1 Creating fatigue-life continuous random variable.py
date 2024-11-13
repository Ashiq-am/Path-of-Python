from scipy.stats import fatiguelife

numargs = fatiguelife.numargs
[a] = [0.7, ] * numargs
rv = fatiguelife(a)

print ("RV : \n", rv)
