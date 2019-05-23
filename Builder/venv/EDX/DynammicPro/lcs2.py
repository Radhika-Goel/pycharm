def lcs(u, v):
	"""Return c where c[i][j] contains length of LCS of u[i:] and v[j:]."""
	c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
	lcs_helper(u, v, c, 0, 0)
	return c


def lcs_helper(u, v, c, i, j):
	"""Return length of LCS of u[i:] and v[j:] and fill in table c.

	c[i][j] contains the length of LCS of u[i:] and v[j:].
	This function fills in c as smaller subproblems for solving c[i][j] are
	solved."""
	if c[i][j] >= 0:
		return c[i][j]

	if i == len(u) or j == len(v):
		q = 0
	else:
		if u[i] == v[j]:
			q = 1 + lcs_helper(u, v, c, i + 1, j + 1)
		else:
			q = max(lcs_helper(u, v, c, i + 1, j),
					lcs_helper(u, v, c, i, j + 1))
	c[i][j] = q
	print("q is",q)
	return q


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


# u = input('Enter first string: ')
# v = input('Enter second string: ')
# c = lcs(u, v)
# print('Longest Common Subsequence: ', end='')
# print_lcs(u, v, c)

if __name__=="__main__":
	with open('5_4_lcs2.in') as fin:
		str1 = fin.readline().strip()
		str2 = "".join(fin.readline().strip().split(" "))
		str3 = fin.readline().strip()
		str4 = "".join(fin.readline().strip().split(" "))
		print(str2)
		print(str4)
		value=lcs(str2,str4)
		print(value)
		print_lcs(str2,str4,value)