def mergeSort(arr):
	value = 0
	if len(arr) <= 1:
		return value
	else:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		#print("L is ",L)
		#print("R is",R)
		value = mergeSort(L) + value
		value = mergeSort(R) + value
		i = 0
		j = 0
		k = 0
		mergearray = []
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				mergearray.append(L[i])
				i+=1
				k+=1
			else:
				mergearray.append(R[j])
				j+=1
				k+=1
				value+=1
		while i < len(L):
			mergearray.append(L[i])
			i+=1
			k+=1
		while j < len(R):
			mergearray.append(R[j])
			k+=1
			j+=1
		return value
		#print(mergearray)


if __name__=="__main__":
	with open('4_4_inversions.in') as fin:
		line = fin.readline().strip()
		W = int(line)
		array_list = fin.readline().split(" ")
		print(mergeSort(array_list))



