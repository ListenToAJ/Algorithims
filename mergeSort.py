import random # Just for generating random lists to sort

#~ Merge function for piecing lists back together
def merge(left, right, parent):
    leftBucket = left
    rightBucket = right
    output = []

    leftIndex = 0
    rightIndex = 0

    #- Here we slowly build out our sorted lists
    while(len(output) < len(parent)):
        #' Once either list has been exhausted we can safely append the other lists leftovers
        if leftIndex == len(leftBucket):
            output += rightBucket[rightIndex:]
            continue
        elif rightIndex == len(rightBucket):
            output += leftBucket[leftIndex:]
            continue
        
        #' We start at the front of each of the two lists and compare
        if leftBucket[leftIndex] <= rightBucket[rightIndex]:
            output.append(leftBucket[leftIndex])
            leftIndex = leftIndex + 1
        else:
            output.append(rightBucket[rightIndex])
            rightIndex = rightIndex + 1

    #- Outputting our now sorted list
    parent[:] = output

#~ Mergesort recursive function for breaking lists apart
def mergeSort(arr):
    #~ Divide / Split up array and recursively call itself
    firstHalf = arr[:len(arr)//2]
    secondHalf = arr[len(arr)//2:]
    if len(arr) > 2:
        mergeSort(firstHalf)
        mergeSort(secondHalf)
    
    #~ Base case
    merge(firstHalf, secondHalf, arr)

#~ Driver Code
arr = random.sample(range(1, 100), 20)
print("Your pre-sorted list is:  " + str(arr))
mergeSort(arr)
print("\n\nYour post sorted list is: " + str(arr))

#* Code / Comments by me