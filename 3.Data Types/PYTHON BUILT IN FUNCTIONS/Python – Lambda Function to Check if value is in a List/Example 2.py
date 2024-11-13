arr=[1,2,3,4]
v=8
x=lambda arr,v: True if v in arr else False

if(x(arr,v)):
    print("Element is Present in the list")
else:
    print("Element is Not Present in the list")
