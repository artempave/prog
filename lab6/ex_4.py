def partition(A, left, right):
    i = left + 1
    j = right
    if left >= right:
        return left
    while i <= j:
        while i <= right and A[i] < A[left]:
            i += 1
        while j > left and A[j] > A[left]:
            j -= 1
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    A[left], A[j] = A[j], A[left]
    return j

if __name__ == '__main__':
    l = input().split()
    A = list(map(int, input().split()))
    index = partition(A, int(l[0]), int(l[1]))
    print(" ".join(map(str, A)))
    print(index)