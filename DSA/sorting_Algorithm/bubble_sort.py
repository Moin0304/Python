def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        for j in range(i):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
A = [8,9,6,7,5,8,3,5]
print("before sorting",A)
bubble_sort(A)
print("after sorting :",A)