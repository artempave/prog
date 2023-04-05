from functools import reduce


def HammingDistance(s1, s2):
    return reduce(lambda x, y: x + (1 if y[0] != y[1] else 0), zip(s1, s2), 0)


def Neighbours(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {"C", "G", "A", "T"}
    Neighborhood = set()
    SuffixNeighbors = Neighbours(Pattern[1:], d)
    for i in SuffixNeighbors:
        if HammingDistance(i, Pattern[1:]) < d:
            for x in {'A', 'C', 'G', 'T'}:
                Neighborhood.add(x + i)
        else:
            Neighborhood.add(Pattern[0] + i)
    return Neighborhood


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


def FrequentWordsWithMismatches(text, k, d):
    FrequentPatterns = []
    Index = []
    l = len(text)
    for i in range(l - k + 1):
        help_arr = list(Neighbours(text[i:i + k], d))
        for dna in help_arr:
            Index.append(PatternToNumber(dna))

    Index.sort()
    SortedIndex = list(Index)
    Count = [1]
    l = len(SortedIndex)
    # Цикл, который за один проход заполняет массив Count, используя SortedIndex
    for i in range(1, l):
        if SortedIndex[i] == SortedIndex[i - 1]:
            Count.append(Count[i - 1] + 1)
        else:
            Count.append(1)
    maxCount = max(Count)
    FrequentPatterns = list(
        map(lambda x: NumberToPattern(SortedIndex[x[0]], k), filter(lambda i: i[1] == maxCount, enumerate(Count))))
    return FrequentPatterns


arr = input()
n = input().split()
ans = FrequentWordsWithMismatches(arr, int(n[0]), int(n[1]))
print(" ".join(ans))
