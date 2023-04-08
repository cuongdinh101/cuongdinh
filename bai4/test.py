text = input("Nhập chuỗi: ")
text_out= text.split()
tim = []

for i in text_out:
    if text_out.count(i) > 1:
        if i not in tim:
            tim.append(i)

if len(tim) == 0:
    print("Không có từ nào lặp lại trong chuỗi.")
else:
    print("Các từ lặp lại trong chuỗi là: " + ", ".join(tim))
