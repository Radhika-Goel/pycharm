#!/usr/bin/python3


#
# def knapsack_problem(W,n,val):
# 	matrix = [[0 for x in range(W+1)] for x in range(n+1)]
#
# 	for i in range(n+1):
# 		for j in range(W+1):
# 			matrix[i][j] = matrix[i-1][j]
# 			if val[i-1] <= W:
# 				print(val[i-1])
# 				value = matrix[i-1][j - val[i-1]] + val[i-1]
# 				if value > matrix[i][j]:
# 					matrix[i][j] = value
# 	return (matrix[n][W])



def knapsack_problem(W,n,val,wt):
	matrix = [[0 for x in range(W+1)] for x in range(n+1)]
	#print (matrix)

	#print('\n'.join(['\t'.join([str(i) for i in y]) for y in matrix]))
	for i in range(n+1):
		for j in range(W+1):
			if i == 0 or j == 0:
				matrix[i][j] = 0
			elif wt[i-1] <= j:
				matrix[i][j] = max(val[i-1]+matrix[i-1][j-wt[i-1]],matrix[i-1][j])
			else:
				matrix[i][j] = matrix[i-1][j]
	return (matrix[n][W])


if __name__=="__main__":
	values1 =[]
	with open('6_1_knapsack.in') as fin:
		line = fin.readline().strip().split(" ")[0]
		#W = int(line.split()[1])
		#print (line)
		W = int(line)
		values = list(map(int,fin.readline().strip().split(" ")))
		print(knapsack_problem(W, len(values), values))

