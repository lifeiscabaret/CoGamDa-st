'''
a = int(input("정수를 입력하세요: "))

while a != 0:
    if a == 0:
        break
        print("종료")
    print(a)
'''

# 오답 무한루프 수정 while True 사용
while True:
    a = int(input("입력: "))
    
    if a == 0:
        break
    print(a)

print("종료")