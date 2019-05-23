#!/usr/local/bin/python3
import operator


weight_value = []
def knapsack_problem(W , weights , values1):
    Total_Value = 0
    for i in range(0,len(weights)):
        weight_value.append({'value':values1[i],'weight':weights[i], 'fraction': values1[i]/weights[i]})
    weight_value.sort(key=operator.itemgetter('fraction'),reverse=True)
    #print (weight_value)
    for i in weight_value:
        if i['weight'] >= W:
            Total_Value = i['fraction'] * W + Total_Value
            print ("First Loop",Total_Value)
            break
        else:
            Total_Value = i['value'] + Total_Value
            print ("Else Loop" , Total_Value)
            W = W - i['weight']
    return Total_Value

if __name__=="__main__":
    weights = []
    values1 =[]
    with open('3_2_loot.in') as fin:
        line = fin.readline()
        W = int(line.split()[1])
        my_fin = fin.readlines()
        #print (my_fin)
        #print (my_fin.__next__())
        #output = my_fin.splitlines()
        #print (output)
        for line in my_fin:
            #print (type(line))
            #line = list(line)a
            line = line.rstrip()
            list1 = line.split(" ")
            #print (list1)
            weights.append(int(list1[1]))
            values1.append(int(list1[0]))
            #print (list2)
    #print (weights)
    #print (values1)

    print (knapsack_problem(W , weights , values1))

