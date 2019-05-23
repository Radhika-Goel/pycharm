def majorityElem(arr):
	lenarr = len(arr)
	dict1 = {}
	total_values=0
	for i in arr:
		if i in dict1:
			dict1[i] += 1
		else:
			dict1[i] = 1
	print(dict1)
	for count in dict1.values():
		if count > lenarr/2:
			total_values += 1
	print(total_values)




if __name__=="__main__":
	weights = []
	values1 =[]
	with open('4_2_majority_element.in') as fin:
		line = fin.readline().strip()
		W = int(line)
		value_per_click = fin.readline().split(" ")
		majorityElem(value_per_click)