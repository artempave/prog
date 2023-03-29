def sort(arr):
    l = len(arr)
    for i in range(l - 1):
        min_ = min(arr[i:])
        a = arr[arr.index(min_)]
        arr[arr.index(min_)] = arr[i]
        arr[i] = a
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))

