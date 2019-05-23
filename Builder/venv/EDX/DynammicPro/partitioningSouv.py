def findPartition(arr,n):
	sum = 0
	i , j = 0 , 0

	for i in range(n):
		sum += arr[i]

	if sum % 2 != 0:
		return 1

	part = [[True for i in range(n+1)] for j in range(sum//2 + 1)]

	for i in range(0,n+1):
		part[0][i] = True

	for i in range(1,sum//2+1):
		part[i][0] = False

	for i in range(1,sum//2 + 1):
		for j in range(1, n + 1):
			part[i][j] = part[i][j - 1]
			if i >= arr[j - 1]:
					  part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
	#print(part[sum//2][n])
	if part[sum//2][n]:
		return 0
	else:
		return 1



if __name__=="__main__":
	values1 =[]
	with open('6_2_souvenirs.in') as fin:
		line = fin.readlines()
		i=0
		while i <= len(line)-2:
			number=int(line[i].strip('\n'))
			data = line[i+1].strip('\n').split(" ")
			data = [int(x) for x in data]
			i += 2
			value = findPartition(data,number)
			values1.append(str(value))
	print(values1)
	print("".join(values1))
