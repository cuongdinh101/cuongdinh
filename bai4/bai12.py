text = input("Nhập chuỗi: ")
tim = []

for i in range(len(text) - 1):
    if text[i] == text[i+1]:
        if text[i] not in tim:
            tim.append(text[i])

if len(tim) == 0:
    print("Không có từ nào lặp lại trong chuỗi.")
else:
    print("Các từ lặp lại trong chuỗi là: " + ", ".join(tim))
