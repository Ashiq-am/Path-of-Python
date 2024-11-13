# import codecs and IncrementalEncoder
import codecs
from codecs import IncrementalEncoder

s = 'GeeksForGeeks'
obj = IncrementalEncoder()

# Using IncrementalEncoder.encode() method
gfg = obj.encode(s)

print(gfg)
