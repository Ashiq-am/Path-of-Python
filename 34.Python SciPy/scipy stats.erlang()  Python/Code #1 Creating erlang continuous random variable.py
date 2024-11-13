from scipy.stats import erlang

numargs = erlang.numargs
[a] = [0.6, ] * numargs
rv = erlang(a)

print ("RV : \n", rv)
