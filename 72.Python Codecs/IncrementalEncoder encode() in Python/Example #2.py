# import codecs and IncrementalEncoder
import codecs
from codecs import IncrementalEncoder

s = 'This is Python in real world'
obj = IncrementalEncoder()

# Using IncrementalEncoder.encode() method
gfg = obj.encode(s)

print(gfg)
