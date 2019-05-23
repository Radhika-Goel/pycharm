def lcs(list1, list2,list3, m, n,o):
	# Create a table to store results of subproblems
	dp = [ [[ 0 for i in range(o + 1) ] for j in range(n + 1)] for k in range(m+1)]
	#dp = [[None for x in range(n+1)] for x in range(m+1)]
	# Fill d[][] in bottom up manner
	for i in range(m+1):
		for j in range(n+1):
			for k in range(o+1):
				if i == 0:
					dp[i][j][k] = 0    # Min. operations = j
				elif j == 0:
					dp[i][j][k] = 0
				elif k == 0:
					dp[i][j][k] = 0
				# If last characters are same, ignore last char
				# and recur for remaining string
				elif list1[i-1] == list2[j-1] and list1[i-1] == list3[k-1]:
					dp[i][j][k] = dp[i-1][j-1][k-1] + 1

			# If last character are different, consider all
			# possibilities and find minimum
				else:
					dp[i][j][k] = max(dp[i][j-1][k],        # Insert
							   dp[i-1][j][k],
								  dp[i][j][k-1])    # Replace

	return dp[m][n][o]


def print_lcs(u, v, c):
	"""Print one LCS of u and v using table c."""
	i = j = 0
	while not (i == len(u) or j == len(v)):
		if u[i] == v[j]:
			print(u[i], end='')
			i += 1
			j += 1
		elif c[i][j + 1] > c[i + 1][j]:
			j += 1
		else:
			i += 1

if __name__=="__main__":
	with open('5_5_lcs3.in') as fin:
		str1 = fin.readline().strip()
		str2 = "".join(fin.readline().strip().split(" "))
		str3 = fin.readline().strip()
		str4 = "".join(fin.readline().strip().split(" "))
		str5 = fin.readline().strip()
		str6 = "".join(fin.readline().strip().split(" "))
		print(str2)
		print(str4)
		print(str6)
		value=lcs(str2,str4,str6,len(str2),len(str4),len(str6))
		print(value)
	#print_lcs(str2,str4,value)