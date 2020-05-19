#Asad Siddiqui
#Quicksort algorithm in Python


def partition(array, low, high):
    i = (low-1) #index for smaller element
    pivot = array[high]

    for j in range(low,high):
        if(array[j] < pivot):
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

#Function to do the quicksort
def quickSort(array,low,high):
    if low < high:

        p = partition(array,low,high)

        #Sorts elements before and after partition
        quickSort(array, low, p-1)
        quickSort(array, p+1, high)


#uncomment which array you want to check
#array = [0,1,1,4,9,6]
array = [0,1,0,1,0,1]
n = len(array)
quickSort(array, 0, n-1)
print("The sorted array is: ")
for i in range(n):
    print(array[i])

