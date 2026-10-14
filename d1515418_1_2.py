A = int(input("輸入數字"))
B = int(input("輸入數字"))
if A>1 or A<0 or B>1 or B<0:
    print("輸入錯誤")
elif A==1 or B==1:
    print("OR=1")
elif A==0 and B==0:
    print("OR=0")
if  A==1 and B==1:
    print("AND=1")
else:
    print("AND=0")
if  A!=B:
    print("XOR=1")
elif A==B:
    print("XOR=0")