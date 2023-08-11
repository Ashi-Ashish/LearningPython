def shellSort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2

A = [30,50,80,90,60,20]
print('Original Aay:', A)
shellSort(A)
print('Sorted Aay:', A)
