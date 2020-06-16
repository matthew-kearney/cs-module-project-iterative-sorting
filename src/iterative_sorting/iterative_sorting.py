# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here
        #Find the index of the smallest in the remaining array
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        if smallest_index != cur_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index] 
    return arr

        # #Now swap the smallest value with the value at cur_index
        #     #store the value for the swap
        # smallest_value = arr[smallest_index]
        #     #set the former smallest value for the current index value
        # arr[smallest_index] = arr[cur_index]
        #     #now go fill in that saved value at the current index
        # arr[cur_index] = smallest_value  
        
    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # First, we determine the length of the array for the for loop we will run 
    arr_len = len(arr)

    # Next, we set the for loop to run up to the last index, aka (arr_len - 1)
    for i in range(arr_len - 1):
        # Then we create a nested for loop that starts at the beginning of the array and goes through the remaining array elements: (arr_len - i -1) represents the length of the array minus the number of elements already sorted by the first for loop
        for j in range(0, arr_len - i - 1):
            # Next, for each element, we check to see if the value at the current index is greater than the value to the right of it
            if arr[j] > arr[j + 1]:
                # If the current value is greater than the one to the right, we swap the elements before resuming the for loop
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
