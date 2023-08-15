def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi-1)
        quickSort(A, pi+1, high)

def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high

    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            print('Changing Array: ', A, 'i,j')
        else:
            break
    A[low], A[j] = A[j], A[low]
    print('Changing Array: ', A)
    return j

A = [3,4,8,9,6,2]
print('Original Array: ', A)
quickSort(A, 0, len(A) - 1)
print('Original Array: ', A)
