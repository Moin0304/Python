def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        pos = i
        for j in range(i+1,n):
            if A[j] < A[pos]:
                pos = j
        temp = A[i]
        A[i] = A[pos]
        A[pos] =temp
A = [3,5,8,9,6,2]
selection_sort(A)
print("sorted Array:",A)

