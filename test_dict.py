def most_count(char):
    split = list(char)
    countsdict = {}
    for ch in split:
        if ch in countsdict:
            count = countsdict[ch]
            countsdict[ch] = count + 1
        else:
            countsdict[ch] = 1

    from collections import Counter
    h = Counter(countsdict)

    high = h.most_common(2)
    print(high)

    print(countsdict)


most_count("hello")
