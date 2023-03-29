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

if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))
