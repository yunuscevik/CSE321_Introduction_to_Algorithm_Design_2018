#########################
# 141044080 Yunus CEVIK #
#########################

# This function sorts the elements of the divided array into two as right and left and combines them into a single sequence.
def merge(leftOfArray, rightOfArray):
    leftOfArray_index = 0
    rightOfArray_index = 0
    result = []
    while leftOfArray_index < len(leftOfArray) and rightOfArray_index < len(rightOfArray):
        if leftOfArray[leftOfArray_index] < rightOfArray[rightOfArray_index]:
            result.append(leftOfArray[leftOfArray_index])
            leftOfArray_index += 1
        else:
            result.append(rightOfArray[rightOfArray_index])
            rightOfArray_index += 1

    result += leftOfArray[leftOfArray_index:]
    result += rightOfArray[rightOfArray_index:]
    return result

# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves as left and right of array, 
# calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves.
def mergeSort(array):

    if len(array) <= 1:  
        return array
        
    half = len(array) // 2
    leftOfArray = mergeSort(array[:half])
    rightOfArray = mergeSort(array[half:])

    return merge(leftOfArray, rightOfArray)


# This function combines the kxn array into a single array, then sorting must be with one of the sort algorithms 
# that are appropriate to the divide and conquer algorithm.
def sortOf2DArray(array):
    singleList = []
    for itemList in array:
        singleList += itemList

    return mergeSort(singleList)


def main():
    k = 7
    n = 4
    array = []
    for i in range(k):
        temp = []
        for j in range(n):
            temp.append(i*3+j*5)
        array.append(temp)

    print("Array(kxn): ", array)
    print()
    print("Sorted Array: ",sortOf2DArray(array))

if __name__ == '__main__':
    main()