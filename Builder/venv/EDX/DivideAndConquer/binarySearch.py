#!/usr/bin/python

def binary_search(number,a):
	min = 0
	max = len(a)-1
	find = False
	count = len(a)
	if number == a[0]:
		return 0
	while count > 1 and not find :
		mid = (min + max)//2
		if number == a[mid]:
			find = True
			return mid
		elif number > a[mid]:
			min = mid + 1
		elif number < a[mid]:
			max = mid - 1
		count = count - 1
	if count == 1:
		return -1


arr1=[1,5,8,12,13]
value = binary_search(2,arr1)
print(value)

