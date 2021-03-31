## Viva 1

## Part 1
## Counting sort

def CountingSort (mylist, maximum):
    max = maximum+1   # need to calculate maximum + 1 because in counting sort we need to have from index = 1

    outputlist = [0] * len(mylist)
    countArray = [0] * max
    runningSumArray = [0] * max

    for i in mylist:
        countArray[i] = countArray[i] + 1       # increasing the count for each specific number in the list

    total = 0
    for i in range(max):
        oldCount = countArray[i]
        runningSumArray[i] = total              # calculating the running sum array
        total += oldCount

    for i in mylist[::-1]:
        outputlist[runningSumArray[i]] = i           # outputting the number in the list to the correct position
        runningSumArray[i] = runningSumArray[i]-1    # minus 1 from that position in the running sum array

    return outputlist

def countingSortRadix(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place      # integer division operator //
        count[index % 10] += 1

    # Calculate running sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSortRadix(array, place)
        place *= 10

    return array

if __name__ == '__main__':
    A = [84, 23, 62, 44, 16, 30, 95, 51]
    #print (CountingSort(A, max(A)))
    print(radixSort(A))