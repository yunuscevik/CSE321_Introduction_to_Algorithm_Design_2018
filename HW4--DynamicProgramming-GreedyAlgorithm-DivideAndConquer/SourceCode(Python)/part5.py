#########################
# 141044080 Yunus CEVIK #
#########################

# There are an array of strings that are defined as equality constraints and inequality constraints, 
# and there are a set of dictionary in which the variables are located. While the variables are "key" in this dictionary, 
# the values are in the "value" section. Strings in the array with conditions are navigated with a "for loop" 
# and whether conditions are successful or unsuccessful according to the values in the dictionary. 
# In order to get the most optimal result in the Greedy algorithm, if one of the conditions does not even suitable, 
# "False" is returned and the function is exited. If all conditions are suitable, then "True" is returned.
def isSatisfied(m,n):
	for itemOfList in m:
		splitEqualValues = itemOfList[0].split("=")
		splitNotEqualValues = itemOfList[0].split("!=")
		if(splitEqualValues != itemOfList and splitNotEqualValues == itemOfList):
			if(n[splitEqualValues[0]] != n[splitEqualValues[1]]):
				return False
		else:
			if(n[splitNotEqualValues[0]] == n[splitNotEqualValues[1]]):
				return False
	return True


def main():
	strList1 = [["x1=x2"],["x2!=x3"],["x3=x4"],["x1=x5"],["x2=x5"],["x4!=x6"] ]
	strList2 = [["x1=x2"],["x2=x3"],["x3=x4"],["x1=x4"],["x2!=x5"],["x4!=x6"] ]

	dict = {"x1":7,"x2":7,"x3":4,"x4":4,"x5":7,"x6":10,"x7":40,"x8":-1,"x9":25}

	print("dictionary: ",dict)
	print("strList 1: ",strList1, " is ", isSatisfied(strList1,dict))
	print()
	print("strList 2: ",strList2, " is ", isSatisfied(strList2,dict))

if __name__ == '__main__':
	main()