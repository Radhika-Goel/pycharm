def lottery(array_list):
	print(array_list)

if __name__=="__main__":
	weights = []
	values1 =[]
	with open('4_5_lottery.in') as fin:
		line = fin.readline().strip().split(" ")[0]
		print(line)
		lottery_numbers = fin.readline().split(" ")
		lottery(array_list)
