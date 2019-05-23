def merge(arrayList,arr1,arr2):
	i = j = k = 0
	mergearray = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arrayList[k] = arr1[i]
			i+=1
			k+=1
		else:
			arrayList[k] = arr2[j]
			j+=1
			k+=1
	while i < len(arr1):
		arrayList[k] = arr1[i]
		i+=1
		k+=1
	while j < len(arr2):
		arrayList[k] = arr2[j]
		k+=1
		j+=1
	print(arrayList)


def mergeSort(array1):
	newList = []
	if len(array1) == 1:
		return array1
	else:
		mid = len(array1)//2
		L = array1[:mid]
		R = array1[mid:]
		mergeSort(L)
		mergeSort(R)
	merge(newList,L,R)


if __name__=="__main__":
	weights = []
	values1 =[]
	with open('4_4_inversions.in') as fin:
		line = fin.readline().strip()
		W = int(line)
		array_list = fin.readline().split(" ")
		#print(array_list)
		mergeSort(array_list)

#arr = [40,20,60,12,5,13]
#n = len(arr)
#mergeSort(arr)
#print ("Sorted array is:")
#for i in range(n):
#	print ("%d" %arr[i]),