def selectionsort(arr):
	for i in range(0,len(arr)):
		minValue = i
		for j in range(i+1,len(arr)):
			if arr[minValue] > arr[j]:
				minValue = j
		temp = arr[i]
		arr[i] = arr[minValue]
		arr[minValue] = temp
	print(alist)


alist = [54,26,93,17,77,31,44,55,20]
selectionsort(alist)
