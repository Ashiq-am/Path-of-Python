'''


'''


"""
>>> nums = [1,2,3,4,5] # list 
>>> name = "Alexander"
>>> details = {"name": "Hemkesh", "age": 23, "active": True} 
>>> 
>>> # Using len() 
... 
>>> len(nums) 
5
>>> len(name) 
9
>>> len(details) 
3
>>> 
>>> # Using str() 
... 
>>> str(12) 
'12'
>>> str(nums) 
'[1, 2, 3, 4, 5]'
>>> str(details) 
"{'active': True, 'age': 23, 'name': 'Hemkesh'}"
>>> 
>>> # Using abspath() 
... 
>>> import os 
>>> os.listdir(".") 
['Django', 'Prep', 'python-the-snake'] 
>>> os.path.abspath("./Django") # pass ".\Django" on windows 
'/Users/admin/projects/Python/Django'
>>> os.path.abspath("Django") 
'/Users/admin/projects/Python/Django'
>>> 
>>> # Using enumerate() 
... 
>>> enumerate(nums) 
<enumerate object at 0x100620b90> 
>>> 
>>> for index, item in enumerate(nums): 
...	 print index, item 
... 
0 1
1 2
2 3
3 4
4 5
>>> 
>>> # Using list() 
... 
>>> list() 
[] 
>>> list(details ) 
['active', 'age', 'name'] 
>>> list(name) 
['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r'] 
>>> 
>>> # Using isfile() & isdir() 
... 
>>> os.path.isdir("Django") 
True
>>> os.path.isfile("Django") 
False
>>> 
>>> os.path.isdir("./python-the-snake/README.md") 
False
>>> os.path.isfile("./python-the-snake/README.md") 
True
>>> 
>>> # Using append() 
... 
>>> nums.append(12) 
>>> nums 
[1, 2, 3, 4, 5, 12] 
>>> nums.append(67) 
>>> nums 
[1, 2, 3, 4, 5, 12, 67] 
>>> 
>>> # Don't press "Run on IDE" button available on right. You will get error 
... # as the statements are already executed on interactive terminal. 
... 
>>> 



"""