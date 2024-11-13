# Python3 code to demonstrate working of
# Strip Punctuations from String
# Using loop + punctuation
from string import punctuation

# initializing string
test_str = '%$Gfg is b !! est(*^&*'

# printing original string
print("The original string is : " + str(test_str))

# getting first non-pnc idx
frst_np = [idx for idx in range(len(test_str)) if test_str[idx] not in punctuation][0]

# getting rear non-pnc idx
rear_np = [idx for idx in range(len(test_str) - 1, -1, -1) if test_str[idx] not in punctuation][0]

# spittd string
res = test_str[frst_np : rear_np + 1]

# printing result
print("The stripped string : " + str(res))
