'''
@Radhika Goel

'''
def moneychange(listCoins,change_need,knownresults):
	minCoins = change_need
	if change_need in listCoins:
		knownresults[change_need] = 1
		return 1
	elif knownresults[change_need] > 0:
		return knownresults[change_need]
	else:
		for i in [c for c in listCoins if c <= change_need]:
			numofCoins = 1 + moneychange(listCoins,change_need - i , knownresults)
			#numofCoins = 1 + moneychange(listCoins,change_need-i)
			if numofCoins < minCoins:
				minCoins = numofCoins
				knownresults[change_need] = minCoins
	return minCoins


a=[1,3,4]
list_coins=[0]*951
total_value = moneychange(a,950,list_coins)
print(total_value)



#DynammicProgramming
def dpmakechange(listCoins,change_need,minCoins):
	for cents in range(change_need+1):
		coinCount = cents
		for j in [c for c in listCoins if c <= cents]:
			if minCoins[cents-j] + 1 < coinCount:
				print("in loop",j)
				coinCount = minCoins[cents-j]+1
		minCoins[cents] = coinCount
	return minCoins[change_need]
a=[1,3,4]
list_coins=[0]*951
total_value = dpmakechange(a,950,list_coins)
print(total_value)

