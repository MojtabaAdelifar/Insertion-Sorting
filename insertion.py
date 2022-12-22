

# insertion sort
def insertionSort(array):
    # loops through the entire array from index[1]
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # loops through the elements before the key element
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1

        # after sorting the key
        # the index after sorted list in array
        array[j + 1] = key

    return array


list = [2, 1, -1, 0, 5, 10]

print(insertionSort(list))