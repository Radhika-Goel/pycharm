#!/usr/bin/python

product= [0] * 9
print(product)
A = [1,2,3]
B= [4,5,6]

for i in range(0,3):
	for j in range(0,3):
		product[i+j] = product[i+j] + A[i] * B[j]
print(product)