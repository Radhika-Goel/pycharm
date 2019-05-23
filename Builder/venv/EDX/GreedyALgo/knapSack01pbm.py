#!/usr/bin/python

# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)

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





    #print (knapsack_problem(W , weights , values1))
if __name__=="__main__":
    weights = []
    values1 =[]
    num_lines = 0
    with open('3_4_covering_segments.in', 'r') as f:
        for line in f:
            num_lines += 1
    print("Number of lines:")
    print(num_lines)
    with open('3_4_covering_segments.in') as fin:
        line = fin.readline().strip()
        #W = int(line.split()[1])
        #print (line)
        W = int(line)
        my_fin = fin.readlines()
        #print (my_fin)
        #print (my_fin.__next__())
        #output = my_fin.splitlines()
        #print (output)
        for line in my_fin:
            #print (type(line))
            #line = list(line)
            #print (line)
            line = line.rstrip()
            list1 = line.split()
            #print (list1)
            #print (list1)
            weights.append(int(list1[0]))
            values1.append(int(list1[1]))
            #print (list2)
    print (weights)
    print (values1)

    print (knapsack_problem(W , num_lines-1, values1,weights ))

