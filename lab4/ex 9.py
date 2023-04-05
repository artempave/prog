def sort(h, arr):
    l = len(arr)
    new_arr = [0 if 10 ** (h) > i else int(str(i)[len(str(i)) - h - 1:len(str(i)) - h]) for i in arr]
    k = max(new_arr)
    B = [0 for _ in range(l)]
    C = [0 for _ in range(k + 1)]
    R = [0 for _ in range(k + 1)]
    for i in range(l):
        C[new_arr[i]] += 1
    R[0] = C[0]
    for i in range(1, k + 1):
        R[i] = R[i - 1] + C[i]
    for i in range(l - 1, -1, -1):
        R[new_arr[i]] -= 1
        B[R[new_arr[i]]] = arr[i]
    return B


def big_sort(arr):
    max_arr = max(arr)
    max_raz = 0
    while (max_arr != 0):
        max_arr //= 10
        max_raz += 1
    for i in range(max_raz):
        arr = sort(i, list(arr))
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    arr = input().split()
    big_sort(list(map(int, arr)))
