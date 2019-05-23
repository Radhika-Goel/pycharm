#!/usr/bin/puthon

def knapsack(W, n , V, wt):
    if n == 0  or W == 0:
        return  0
    #If weight of nth item is more than capacity of Knapsack W , then this item cannot added in optimal solution
    if (wt[n-1] > W):
        return knapsack(W , wt , V , n -1 )
    else:
        #return 2 possible Cases
        #1. nth item included
        #2. not included
        return max(V[n-1] + knapsack(W - wt[n-1] , n-1 , V , wt ), knapsack(W , n-1 , V , wt))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print (knapsack(W , n , val , wt))