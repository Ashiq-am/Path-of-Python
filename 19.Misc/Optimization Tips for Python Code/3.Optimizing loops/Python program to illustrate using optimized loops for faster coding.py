# Python program to illustrate using
# optimized loops for faster coding

# slow O(n^2) - ( Note: In latest implementations it is O(n) )
from urllib3.connectionpool import xrange

s = 'hellogeeks'
slist = ''
for i in s:
    slist = slist + i
print(slist)

# string concatenation (idiomatic and fast O(n))
st = 'hellogeeks'
slist = ''.join([i for i in s])
print(slist)

# Better way to iterate a range
evens = [i for i in xrange(10) if i % 2 == 0]
print(evens)

# Less faster
i = 0
evens = []
while i < 10:
    if i % 2 == 0: evens.append(i)
    i += 1
print(evens)

# slow
v = 'for'
s = 'geeks ' + v + ' geeks'
print(s)

# fast
s = 'geeks %s geeks' % v
print(s)














"""Every time running a loop to s(i), Python evaluates the method. However, if you place the 
evaluation in a variable, the value is already known and Python can perform tasks faster."""

