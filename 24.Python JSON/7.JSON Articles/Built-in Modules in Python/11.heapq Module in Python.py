import heapq
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

heapq.heapify(numbers)
heapq.heappush(numbers, 7)
print(heapq.heappop(numbers))
print(heapq.heappushpop(numbers, 8))
print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))
