def sort(h, arr):
    l = len(arr)
    for i in range(h, l):
        help_ = arr[i]
        j = i
        while (j >= h and help_ < arr[j-h]):
            arr[j] = arr[j-h]
            j -= h
        arr[j] = help_
        print(" ".join(map(str, arr)))
if __name__ == '__main__':
    h = int(input())
    arr = input().split()
    sort(h, list(map(int, arr)))
