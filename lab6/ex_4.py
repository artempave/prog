def partition(A, left, right):
    i = left + 1
    j = right
    if len(A[left:right+1]) <= 1:
        return left
    while i <= j:
        while A[i] < A[left] and i < right:
            i += 1
        while A[j] > A[left] and j > left:
            j -= 1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        if j != right:
            j -= 1
    A[left], A[j] = A[j], A[left]
    return j

if __name__ == '__main__':
    l = input().split()
    A = list(map(int, input().split()))
    index = partition(A, int(l[0]), int(l[1]))
    print(" ".join(map(str, A)))
    print(index)