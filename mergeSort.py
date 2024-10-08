import random # Just for generating random lists to sort

#~ Merge function for piecing lists back together
def merge(left, right, parent):
    output = []
    leftIndex = 0
    rightIndex = 0

    #- Here we slowly build out our sorted lists
    while(len(output) < len(parent)):
        #' Once either list has been exhausted we can safely append the other lists leftovers
        if leftIndex == len(left):
            output += right[rightIndex:]
            continue
        elif rightIndex == len(right):
            output += left[leftIndex:]
            continue
        
        #' We start at the front of each of the two lists and compare
        if left[leftIndex] <= right[rightIndex]:
            output.append(left[leftIndex])
            leftIndex = leftIndex + 1
        else:
            output.append(right[rightIndex])
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
arr = random.sample(range(1, 20), 10)
print("Your list before sorting: " + str(arr))
mergeSort(arr)
print("\nYour list after sorting:  " + str(arr))

#* Code / Comments by me