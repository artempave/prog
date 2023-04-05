def sort(hs, arr):
    l = len(arr)
    for h in hs:
        for i in range(h, l):
            help_ = arr[i]
            j = i
            while (j >= h and help_ < arr[j - h]):
                arr[j] = arr[j - h]
                j -= h
            arr[j] = help_
        print(" ".join(map(str, arr)))


if __name__ == '__main__':
    hs = input().split()
    arr = input().split()
    sort(list(map(int, hs)), list(map(int, arr)))
