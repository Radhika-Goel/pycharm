def partition(arra,low,high):
	i = (low)
	pivot = arra[low]
	same_index = 0
	for j in range(low+1,high+1):
		if arra[j] <= pivot:
			i = i+1
			arra[i],arra[j] = arra[j],arra[i]

			if arra[j] == pivot:
				same_index += 1
			else:
				arra[i-same_index-1],arra[i] = arra[i],arra[i-same_index-1]
	return (same_index,i)







def quicksort(arr,i,j):
	if i < j:
		(m,n) = partition(arr,i,j)
		quicksort(arr,i,n-m-1)
		quicksort(arr,n+1,j)



arr = [40,20,60,12,5,13,13,13,13]
n = len(arr)
quicksort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %arr[i]),