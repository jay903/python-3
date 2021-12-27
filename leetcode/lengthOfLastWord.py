s="a          "
n = len(s)
l = ""

k = []

for word in range((n - 1)):

    if s[word] == " " and s[word + 1].isalpha():

        k.append(word)
if k:

    f = max(k)
    for j in range((f + 1), n):

        if s[j].isalpha():
            l += s[j]
    print(len(l))
else:
    h=len(s)

    for w in s:

        if w==" ":
            h = h-1
    print(h)

