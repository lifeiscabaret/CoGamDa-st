# for i in range(1, 11):
#     i = (i + 1) * i / 2    
    
#     print(f"누적 합계:", i)

n = int(input("숫자를 입력하시오: "))

for i in range(1, n+1):
    i = (n + 1) * i / 2
    
    print(f"누적 합계:", i)