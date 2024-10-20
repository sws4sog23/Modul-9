def all_variants(text):
    a = text
    b = len(text)
    for n in range(b + 1):
        n = 1 + n
        for i in range(b + 1 - n):
            yield (a[i:i + n])


a = all_variants("abc")
for i in a:
    print(i)