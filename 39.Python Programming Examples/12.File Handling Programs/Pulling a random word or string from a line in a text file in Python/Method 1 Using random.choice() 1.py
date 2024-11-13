# import required module
import random

# print random word
print(random.choice(open("myFile.txt","r").readline().split()))
