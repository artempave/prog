def sort(arr):
    l = len(arr)
    for i in range(l - 1):
        min_ = min(arr[i:])
        c = arr.index(min_)
        a = arr[c]
        arr[c] = arr[i]
        arr[i] = a
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))

