# Python Program illustrating
# numpy.char.decode() method
import numpy as np

arr1 = ['eAAAa', 'ttttds', 'AAtAAt']
arr2 = ['11sf', 'sdsf2', '1111f2']

print ("\narr1 : ", arr1)
print ("\narr2 : ", arr2)

# Using np.char.encode()
encode_arr1 = np.char.encode(arr1, encoding ='cp037')
print ("\nEncoded arr1 : \n", encode_arr1)

encode_arr2 = np.char.encode(arr2, encoding ='utf8')
print ("\nEncoded arr2 : \n", encode_arr2)

# Using np.char.decode()
decode_arr1 = np.char.decode(encode_arr1, encoding ='cp037')
print ("\nDecoded arr1 : \n", decode_arr1)

decode_arr2 = np.char.decode(encode_arr2, encoding ='cp037')
print ("\nDecoded arr1 : \n", decode_arr2)

decode_arr2 = np.char.decode(encode_arr2, encoding ='utf8')
print ("\nDecoded arr1 : \n", decode_arr2)
