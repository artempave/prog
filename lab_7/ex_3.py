def F(n):
    if n < 2:
        return n
    return F(n - 1) + F(n - 2)

def fibSearch(A, elem):
    if elem < A[0] or elem > A[-1]:
        print(None)
        return None
    k = 0
    while F(k) < len(A):
        k += 1
    return fibSearchRec(A, elem, 0, F(k-1), F(k), len(A))

def fibSearchRec(A, elem, lo, fKm1, fK, n):
    if fK == 0 or (fK == 1 and A[lo] != elem):
        print(A[lo])
        return -1
    if fK == 1 and A[lo] == elem:
        return lo
    fKm2 = fK - fKm1
    mid = min(lo + fKm2 - 1, n - 1)
    print(A[mid], end = " ")
    if A[mid] == elem:
        return mid
    elif A[mid] > elem:
        return fibSearchRec(A, elem, lo, fKm1 - fKm2, fKm2, n)
    else:
        return fibSearchRec(A, elem, lo + fKm2, fKm2, fKm1, n)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    chec = fibSearch(A, elem)