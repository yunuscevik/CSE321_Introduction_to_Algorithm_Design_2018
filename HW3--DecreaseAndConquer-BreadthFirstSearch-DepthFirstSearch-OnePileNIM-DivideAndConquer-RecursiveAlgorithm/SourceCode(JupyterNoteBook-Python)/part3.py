def findFixedPoint(arr, leftValue, rightValue):
    midlePoint = None
    if rightValue >= leftValue: 
        midlePoint = (leftValue + rightValue)//2
    if midlePoint is not None:
        if midlePoint is arr[midlePoint]: 
            return int(midlePoint)

        if midlePoint > arr[midlePoint]: 
            return findFixedPoint(arr, (midlePoint + 1), rightValue) 
        else: 
            return findFixedPoint(arr, leftValue, (midlePoint -1)) 
    else:
        return "There is not Fixed Point"

def main():
    arr = [-10,0,2,10,30,50,110]
    result = findFixedPoint(sorted(arr), 0, len(arr)-1)
    if(isinstance(result, str)):
        print(result)
    else:
        print("Fixed Point is " + str(result))

        
if __name__ == "__main__":
    main()