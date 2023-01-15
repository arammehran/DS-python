"""
Implement quick sort in Python.
"""
# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
size = len(test)
quickSort(test, 0, size - 1)
print(test)

m = [None] * 4
for i in range(len(m)):
    if m[i]:
        continue
    else:
        m[i] = 5
        break
print(m)

