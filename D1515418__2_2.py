A = int(input())
B = int(input())
S = int(input())
middle = 0
start = 0
if A != 0 and A != 1 or B != 0 and B != 1 or S != 0 and S != 1:
    print("輸入錯誤")
else:
    if S == 1:
        middle = A or B
    else:
        middle = A and B

    if middle == 1 and S == 1:
        start = 1
    else:
        start = 0

print(f"第一個輸出={middle}")
print(f"允許啟動={start}") 
