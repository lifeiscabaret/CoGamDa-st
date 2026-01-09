"""
[day10]응용문제 1. 반복 구조로 데이터 처리하기
📌 문제
사용자로부터 정수를 계속 입력받는다.
입력한 값이 0이면 입력을 종료한다.
입력한 값이 음수이면 무시한다.
입력한 값이 양수이면 리스트에 저장한다.
입력이 끝난 뒤,

리스트에 저장된 값 중 짝수의 개수와 짝수의 합을 출력하시오.
📥 입력
정수 여러 개 (한 줄에 하나씩 입력)
0이 입력되면 종료
📤 출력
아래 형식으로 출력한다.
짝수 개수: X
짝수 합계: Y
구현 조건 (필수)
while 반복문 사용
break를 이용해 입력 종료 처리
continue를 이용해 음수 무시
리스트에 값 저장 후 for 반복문으로 처리
반복문 안에서 조건문(if) 사용

"""

inputlayer = []
j = 1
while True:
    i = int(input(f"{j}번째 정수 입력(0이면 종료): "))
    j += 1
    if i == 0:
        break
    elif i < 0:
        continue
    else:
        inputlayer.append(i)
count = 0
sum = 0
for i in inputlayer:
    if i % 2 == 0:
        count += 1
        sum += i
print(f"짝수 개수: {count}")
print(f"짝수 합계: {sum}")
