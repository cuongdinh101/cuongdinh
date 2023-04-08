txt1 = "Abc"
txt2 = "Xyz"
txt3 = ""
l=len(txt1)
for i in range(len(txt1)):
    txt3 += txt1[i] + txt2[i]
print(txt3)
print(l)