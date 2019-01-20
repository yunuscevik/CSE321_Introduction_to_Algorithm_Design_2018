#########################
# 141044080 Yunus CEVIK #
#########################



#The function separates adjacent meaningful words with the help of a dictionary.
def ReconstitutedSentences(s,d):
	s = s.lower()
	sentence = ""
	tempJ = 0
	for i in range(len(s)):
		for j in range(1,len(s)+1):
			if s[i:j] in d and tempJ < j:
				tempJ = j
		if s[i:tempJ] in d:
			sentence += s[i:tempJ] + " "

	return sentence


	
def main():
	s1 = "ThereisaCatandThereisaThedog"
	s2 = "itwasthebestoftimes"
	d = {"the", "there", "of", "car","fish","cat", "dog","is","a","and","it","was","best","times"}
	print("s1: ",s1)
	print("s1 editing: " ,ReconstitutedSentences(s1,d))
	print()
	print("s2: ",s2)
	print("s2 editing: " ,ReconstitutedSentences(s2,d))

if __name__ == '__main__':
    main()