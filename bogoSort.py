import random # Come on you know why we need this
import time

#~ Bogo Sort Function
def bogoSort(arr):
    #- Is list already sorted?
    isSorted = all(b >= a for a, b in zip(arr, arr[1:]))
    iterationCount = 1
    start = time.time()

    #- The meat
    while isSorted == False:
        random.shuffle(arr)
        isSorted = all(b >= a for a, b in zip(arr, arr[1:]))
        print("Iteration #" + str(iterationCount) + ": " + str(arr))
        iterationCount += 1

    print("\nSorted in " + str(round(time.time() - start, 4)) + " seconds.")
    
#~ Driver Code
arr = random.sample(range(1, 20), 5)
print("Your list before sorting: " + str(arr) + "\n")
bogoSort(arr)
print("\nYour list after sorting:  " + str(arr))

#* Code / Comments by me (With some help from stackoverflow on oneliner)