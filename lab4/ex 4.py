def sort(arr):
    l = len(arr)
    flag = 0
    for i in range(l - 1):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = 1
        print(" ".join(map(str, arr)))
        if flag == 0:
            break
        else:
            flag = 0

if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))

