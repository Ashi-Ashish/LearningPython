def mergeSort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid + 1, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left

    B = [0] * (right + 1)

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1

    for x in range(left, right + 1):
        A[x] = B[x]


A = [3, 5, 8, 9, 6, 2]
print('Original Array:', A)
mergeSort(A, 0, len(A) - 1)
print('Sorted Array:', A)
