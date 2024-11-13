file=open("array","wb")
num=[3,6,9,12,18]
array=bytearray(num)
file.write(array)
file.close()
