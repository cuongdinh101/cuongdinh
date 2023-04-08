
txt = "Appleeee"
count = {}
for i in range(len(txt)):
    if txt[i] in count:
        count[txt[i]] += 1
    else:
        count[txt[i]] = 1

for char in count:
    print(char, ":", count[char])

print(txt, "số lần là", len(txt))
