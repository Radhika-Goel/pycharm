#/usr/bin/python2
import sys
n=int(raw_input())
#a = map(int,[raw_input().split() for i in n])
numbers = list(map(int,raw_input().split()))
product = 0
if len(numbers) == n:
    for i in range(0,n):
        for j in range(i+1,n):
            product = max(product,numbers[i]*numbers[j])
    print product
else:
    sys.exit()

####Optimized Approach
import sys
n=int(raw_input())
#a = map(int,[raw_input().split() for i in n])
numbers = list(map(int,raw_input().split()))
product = 0
if len(numbers) == n:
    if numbers[0] > numbers[1]:
        first_larger , second_larger = numbers[0],numbers[1]
    else:
        second_larger,first_larger = numbers[0],numbers[1]
    for i in range(2,n):
        if numbers[i] > second_larger:
            if numbers[i]>first_larger:
                second_larger,first_larger = first_larger,numbers[i]
            else:
                second_larger = numbers[i]
    print first_larger * second_larger
else:
    sys.exit()

###Bookish Approach
import sys
def pairwiseproduct(array1):
    index1,index2=1
    for i in range(2,len(array1)):
        if array1[i] > array1[index1]:
            index1=i
    if index1==1:
        index2=2
    else:
        index2=1
    for i in range(1,len(numbers)):
        if array1[i] != array1[index1] and array1[i] > array1[index2]:
            index2=i
    return array1[index1]*array1[index2]


n=int(raw_input())
#a = map(int,[raw_input().split() for i in n])
numbers = list(map(int,raw_input().split()))
if len(numbers) == n:
    print pairwiseproduct(numbers)
else:
    sys.exit()
