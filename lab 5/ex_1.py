def PatternToNumber(dna):
    book = {"A": 0, "C": 1, "G": 2, "T": 3}
    size_dna = len(dna)
    if size_dna == 0:
        return 0
    char_last = dna[-1]
    dna = dna[:-1]
    return PatternToNumber(dna) * 4 + book[char_last]


def NumberToPattern(index, k):
    book = {0: "A", 1: "C", 2: "G", 3: "T"}
    if k == 1:
        return book[index]
    divider = index // 4
    remainder = index % 4
    return NumberToPattern(divider, k - 1) + book[remainder]


def FrequentWordsWithSorting(text, k):
    FrequentPatterns = []
    Index = []
    l = len(text)
    for i in range(l - k + 1):
        Index.append(PatternToNumber(text[i:i + k]))
    Index.sort()
    SortedIndex = list(Index)
    Count = [1]
    l = len(SortedIndex)
    for i in range(1, l):
        if SortedIndex[i] == SortedIndex[i - 1]:
            Count.append(Count[i - 1] + 1)
        else:
            Count.append(1)
    maxCount = max(Count)
    FrequentPatterns = list(
        map(lambda x: NumberToPattern(SortedIndex[x[0]], k), filter(lambda i: i[1] == maxCount, enumerate(Count))))
    return Count, FrequentPatterns


arr = input()
n = int(input())
ans = FrequentWordsWithSorting(arr, n)
print(" ".join(map(str, ans[0])))
print(" ".join(ans[1]))
