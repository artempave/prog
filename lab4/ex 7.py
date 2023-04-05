def sort(arr):
    book = [0 for _ in range(1000)]
    for i in arr:
        book[i] += 1
    l = len(book)
    for i in range(l):
        if book[i] > 0:
            for j in range(book[i]):
                print(i, end=" ")


if __name__ == '__main__':
    arr = input().split()
    sort(list(map(int, arr)))
