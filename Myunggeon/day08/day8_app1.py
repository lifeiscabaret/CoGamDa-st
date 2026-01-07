#입력 기반 반복(실전)


num = int(input("숫자를 입력하세요: "))

while True:
    print("입력한 숫자는", num, "입니다.")
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break

print("종료")

'''
While True와 break 사용하지 않는 풀이.
'''
num = int(input("숫자를 입력하세요: "))

while num != 0:
    print("입력한 숫자는", num, "입니다.")
    num = int(input("숫자를 입력하세요: "))

print("종료")