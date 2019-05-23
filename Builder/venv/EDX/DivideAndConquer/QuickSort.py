def pi(arra,low,high):
	i = ( low-1 )         # index of smaller element
	pivot = arr[high]     # pivot

	for j in range(low , high):

		# If current element is smaller than or
		# equal to pivot
		if(arr[j] <= pivot):

			# increment index of smaller element
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return ( i+1 )






def quickSort(arr,low,high):

	if low < high:
		value = pi( arr,low,high)
		quickSort(arr,low,value-1)
		quickSort(arr,value+1,high)


arr = [40,20,60,12,5,13]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %arr[i]),