def selection_sort(array):
    n = len(array)
    # assuming the current position as the index of the smallest item
    for i in range(n):
        min_index = i
    # Looking through the unsorted part to make sure which one is really the smallest item
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                # updates when found one
                min_index = j
    # builds the sorted portion by swapping the min item with the item at current position
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


numbers = [6, -5, 0, 1, 8, 7]
print(f"Sorted:{selection_sort(numbers)}")
