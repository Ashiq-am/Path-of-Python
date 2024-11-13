import heapq as hq

# list of dictionaries
li_dict=[{11:121},{2:4},{5:25},{3:9}]

# list to hold tuples
heap_dict=[]

# convert each dict to tuple of (key,value)
heap_dict = [(k,v) for i in li_dict for k,v in i.items() ]

print("List of tuples :",heap_dict)

# applying heapify()
hq.heapify(heap_dict)

print("After heapification :",heap_dict)

# reconvert to dict
final=dict(heap_dict)

print("Dictionary as heap :",final)

# add new value (1,1)
hq.heappush(heap_dict,(1,1))

print("After insertion & heapification",heap_dict)

#reconvert the result
final=dict(heap_dict)

print("New dictionary :",final)
