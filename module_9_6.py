def all_variants(text):
    for k in range(len(text)):
        for j in range(len(text) - k):
            yield text[j: j + k + 1]


a = all_variants("abc")
for i in a:
    print(i)