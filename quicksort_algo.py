def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p-1)
        quick_sort(array, p+1, high)

def partition(array, high, low):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def main():
    array = []
    array_size = int(input('Enter the size of the array: '))
    for i in range(array_size):
        element = int(input())
        array.append(element)

    print('The array before sorting is: ', array)
    quick_sort(array, 0, array_size-1)
    print('The array after sorting is: ', array)

if __name__ == '__main__':
    main()
