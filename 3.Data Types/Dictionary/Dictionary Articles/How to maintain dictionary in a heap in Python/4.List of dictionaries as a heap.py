# import modules
import heapq as hq

# list of dictionaries
li_dict=[{11:121},{2:4},{5:25},{3:9}]

#temporary list to hold tuple of key-value pairs
heap_dict=[]

# conert each dict to tuple
heap_dict = [(k,v) for i in li_dict for k,v in i.items() ]

print("After extraction :",heap_dict)

# heapify the list of tuples
hq.heapify(heap_dict)

print("Heapified key-value pairs :",heap_dict)

# reconvert to dictionary
final=dict(heap_dict)
print("Heapified dictionaries :",final)
