def sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
        print(" ".join(map(str, arr)))


if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))
