def maxLeftAndRightSum(arr, leftValue, middlePoint, rightValue, sumOfValues=0, sumOfLeftValues=-10000, sumOfRightValues=-10000 ): 
    
    for i in range(middlePoint, leftValue - 1, -1): 
        sumOfValues += arr[i]
        if (sumOfValues > sumOfLeftValues): 
            sumOfLeftValues = sumOfValues 
    
    sumOfValues = 0
    for i in range(middlePoint + 1, rightValue + 1): 
        sumOfValues += arr[i] 
        if (sumOfValues > sumOfRightValues): 
            sumOfRightValues = sumOfValues 
        
    return sumOfLeftValues + sumOfRightValues
            


def maxContiguousSubsetSum(arr, leftValue, rightValue): 
    
    if (leftValue == rightValue): 
        return arr[leftValue] 
    
    middlePoint = (leftValue + rightValue) // 2

    return max(maxContiguousSubsetSum(arr, leftValue, middlePoint), 
            maxContiguousSubsetSum(arr, middlePoint + 1, rightValue), 
            maxLeftAndRightSum(arr, leftValue, middlePoint, rightValue))

def main():
    arr = [5, -6, 6, 7, -6, 7, -4, 3]
    result = maxContiguousSubsetSum(arr, 0, len(arr)-1) 
    print("Maximum contiguous sum is ", result)


if __name__ == "__main__":
    main()