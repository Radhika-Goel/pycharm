#!/usr/bin/python

def binary_search(number):
	min = 0
	max = len(arr1)-1
	find = False
	count = len(arr1)
	if number == arr1[0]:
		return 0
	while count > 1 and not find :
		mid = (min + max)//2
		if number == arr1[mid]:
			find = True
			return mid
		elif number > arr1[mid]:
			min = mid + 1
		elif number < arr1[mid]:
			max = mid - 1
		count = count - 1
	if count == 1:
		return -1


arr1=[1,5,8,12,13]
arr2 = []
arr3 = []
for i in arr1:
	value = binary_search(i)
	arr3.append(value)
print(arr3)
print(" ".join(arr3))

