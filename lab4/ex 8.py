def sort(h, arr):
    l = len(arr)
    new_arr = [0 if 10**(h)>i else int(str(i)[len(str(i))-h-1:len(str(i))-h]) for i in arr]
    k = max(new_arr)
    B = [0 for _ in range(l)]
    C = [0 for _ in range(k+1)]
    R = [0 for _ in range(k+1)]
    for i in range(l):
        C[new_arr[i]] += 1
    R[0] = C[0]
    for i in range(1, k+1):
        R[i] = R[i - 1] + C[i]
    for i in range(l-1, -1, -1):
        R[new_arr[i]] -= 1
        B[R[new_arr[i]]] = arr[i]
    print(" ".join(map(str, B)))

if __name__ == '__main__':
    h = int(input())
    arr = input().split()
    sort(h, list(map(int, arr)))
