a = int(input("정수를 입력하시오: "))

if a % 6 == 0:
    print("6의 배수")
elif a % 2 == 0:
    print("2의 배수")
elif a % 3 == 0:
    print("3의 배수")
else:
    print("해당 없음")