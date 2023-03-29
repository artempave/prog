def sort(arr):
    l = len(arr)
    for i in range(1, l):
        help_ = arr[i]
        j = i
        while (j > 0 and help_ < arr[j-1]):
            arr[j ] = arr[j-1]
            j -= 1
        arr[j ] = help_
        print(" ".join(map(str, arr)))


arr = input().split()
sort(list(map(int, arr)))
