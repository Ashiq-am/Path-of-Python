# initialize the list
li = [1, 4, 93, 2, 3, 5]

print("Swaps :")

# loop for arranging
for i in range(0, len(li)):

	for j in range(i+1, len(li)):

		# swap if i>j
		if li[i] > li[j]:
			temp = li[j]
			li[j] = li[i]
			li[i] = temp

			# print swapped elements
			print(li[i], li[j], sep="<--->")

print("Output :", li)
