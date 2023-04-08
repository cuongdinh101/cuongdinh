txt1="America"
txt2= "Japan"
first=txt1[0]+txt2[0]
mid= txt1[int(len(txt1)/2):int(len(txt1)/2)+1] + txt2[int(len(txt2)/2): int(len(txt2)/2)+1]
last=txt1[len(txt1)-1] + txt2[len(txt2)-1]
out_txt= first + mid + last
print(out_txt)