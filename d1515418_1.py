x=int(input("請輸入一個整數:"))
if x<0 or x>15 :
    print("輸入錯誤")
else:
    a1=x%2
    a2=(x//2)%2
    a3 =(x//4)%2
    a4=(x//8)%2
    print(f"二進制: {a4}{a3}{a2}{a1}")
    b1=x%8
    b2=x//8
    print(f"八進制: {b2}{b1}")
    if x < 10:
        print(f"十六進制：{x}")
    elif x == 10:
        print("十六進制：A")
    elif x == 11:
        print("十六進制：B")
    elif x == 12:
        print("十六進制：C")
    elif x == 13:
        print("十六進制：D")
    elif x == 14:
        print("十六進制：E")
    elif x == 15:
        print("十六進制：F")