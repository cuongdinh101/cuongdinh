import re

txt= "Mike30 is a data5 scientist and Al1 expert"
txt_1 = txt.split()

for i in txt_1:
    txt_out = re.findall(r'\w*\d\w*', i)
    if txt_out:
        print(i)
        
