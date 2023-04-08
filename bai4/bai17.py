txt = '/* jon is a @developer & musican!!'
txt_special = '/*@&!'
for char in txt_special:
    txt = txt.replace(char, '#')
print(txt)
