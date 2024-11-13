from itertools import chain

st1 = "Geeks"
st2 = "for"
st3 = "Geeks"

res = list(chain(st1, st2, st3))
print("before joining :", res)

ans = ''.join(res)
print("After joining :", ans)
