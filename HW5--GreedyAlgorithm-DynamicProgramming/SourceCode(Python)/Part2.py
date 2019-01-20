#########################
# 141044080 Yunus CEVIK #
#########################

# This function calculates the minimum cost between cities
def minimumCost(NY,SF,M):
    optN = [NY[0]]
    optS = [SF[0]]
    for i in range(1,len(NY)):
        optN.append(NY[i] + min(optN[i - 1], (M + optS[i - 1])))
        optS.append(SF[i] + min(optS[i - 1], (M + optN[i - 1])))

    return min(optN[len(optN)-1],optS[len(optS)-1])

def main():
	M = 10
	NY = [3, 18, 24, 35, 2, 8, 41]
	SF = [19, 59, 9, 49, 3, 1, 4]

	print("Number of Months (n) : ",len(NY))
	print("Moving Cost (M) : ", M)
	print("------------------------")
	print("NY : ",NY)
	print("SF : ",SF)
	print("------------------------")
	print("The Cost of Optimal Plan: ",minimumCost(NY,SF,M))

if __name__ == '__main__':
	main()