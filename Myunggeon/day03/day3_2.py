#abs()란? 절댓값을 반환하는 파이썬 내장 함수
num = int(input("정수 하나 입력:"))
num_abs = abs(num)

if num_abs == 10:
    print("10")
elif num_abs > 10:
    print("크다")
elif num_abs < 10:
    print("작다")
    