print(" Tam giác ABC có 3 cạnh a, b và c lần lượt là:")
a= float(input("Nhập cạnh a của tam giác vào: "))
b= float(input("Nhập cạnh b của tam giác vào: "))
c= float(input("Nhập cạnh c của tam giác vào: "))

if a + b > c and a + c > b and b + c > a:
    if( a == b == c):
        print("Đây là tam giác đều!")
    elif a == b or b == a or a == c:
        print("Dây là tam giác cân!")
    elif a*a == b*b + c*c or b*b == a*a +c*c or c*c == a*a +b*b:
        print("Đây là tam giác vuông!")
    else:
        print("Đây là tam giác thường!")
else:
    print("bạn nhập sai rồi, nhập lại đi nào!") 
          
        
