arr = [2,8,5,3,9,4]

def insertionSort(arr):
    #- Start at the second item in the list, and move to the right
    for i in range(1, len(arr)):
        #' Focus on one item and have index prepared for its left neighbor
        focus = arr[i]
        j = i - 1

        #' While j is in bounds, and our focused value can go further left
        while j >= 0 and focus < arr[j]:
            
            #- Slide down the array until our focus value can't go further left
            arr[j+1] = arr[j]
            j -= 1
        
        #' Insert our focus value
        arr[j+1] = focus

insertionSort(arr)

#* Code from: Geeksforgeeks, Comments by me
