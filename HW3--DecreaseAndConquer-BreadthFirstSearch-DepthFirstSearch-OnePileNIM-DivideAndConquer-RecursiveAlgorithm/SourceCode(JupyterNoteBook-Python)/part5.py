def ReturnPattern(string, dictionary, newDictionary={}, pattern="", patternVal='A',count=1):
    string = string.lower()
            
    if (len(string) == 0):
        return pattern
    
    subStr = string[0 : count]
    
    if(len(string) < count):
        pattern += str(patternVal)
        return pattern
    
    if subStr in dictionary:
        if subStr in newDictionary:
            pattern += str(newDictionary[subStr])
            return ReturnPattern(string[count:], dictionary, newDictionary, pattern, patternVal, 1)
        else:
            newDictionary[subStr] = patternVal
            pattern += str(patternVal)
            return ReturnPattern(string[count:], dictionary, newDictionary, pattern, chr(ord(patternVal) + 1), 1)
    else:
        return ReturnPattern(string, dictionary, newDictionary, pattern, patternVal, count+1)


def patternCheck(string, pattern, dictionary):
    if pattern == ReturnPattern(string, dictionary):
        return "Pattern is Valid"
    return "Pattern is Invalid"


def main():
    string = "Tobeornottobe"
    dictionary = {"to","be","or","not"}
    pattern = "ABCDAB"
    print(patternCheck(string, pattern, dictionary))

if __name__ == "__main__":
    main()