from scipy.stats import genextreme

numargs = genextreme .numargs
[a] = [0.7, ] * numargs
rv = genextreme (a)

print ("RV : \n", rv)
