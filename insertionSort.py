import random # Just for generating random lists to sort

#~ Single sort function
def insertionSort(arr):
    #- Start at second item
    for i in range(1,len(arr)):
        #' Store it and make a note of position 1 to left
        temp = arr[i]
        j = i-1

        #' Start checking left vals one by one to see if they are bigger
        while j >= 0:
            #- If a value is bigger then our temp, start sliding over vals to make room
            if arr[j] > temp:
                arr[j+1] = arr[j]
            #- If the value to the left is not bigger, we stop and leave it where we are
            else:
                break;
            j -=1
        arr[j+1] = temp

#~ Driver Code
arr = random.sample(range(1, 20), 10)
print("Your list before sorting: " + str(arr))
insertionSort(arr)
print("\nYour list after sorting:  " + str(arr))

#* Code / Comments by me