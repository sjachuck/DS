

arr = [10, 30, 28, 18, 35, 3]

def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def displayArray():
    print " - ".join([str(elem) for elem in arr])

def bubble_sort():
    print "Sorting array"
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swap(j, j+1)
        displayArray()
    print "Sorting Complete..."


if __name__ == '__main__':
    displayArray()
    bubble_sort()
    displayArray()