# 문제
# 정수 하나를 입력받아 다음 조건에 따라 출력하시오.
# 2와 3의 배수 → "6의 배수"
# 2의 배수 → "2의 배수"
# 3의 배수 → "3의 배수"
# 아무것도 아니면 → "해당 없음"
# 조건
# if / elif / else 사용
# 조건 순서 중요

'''
정수 입력 받기.
isdigit써볼까
x%2==0 and x%3==0 이면 6의 배수
x%2==0이면 2의 배수
x%3==0이면 3의 배수
if elif els 사용해야 하므로
6의 배수 먼저하고
2나 3의 배수 elif
남은거 else
'''


# 정수가 아닐때 input을 계속 받게 하려면 isdigit()은 안어울린다.
# try except 구문을 쓰는 것이 정석

while True:
    try:
        num = int(input("정수를 입력하세요: "))
        break # 성공하면 반복종료
    except ValueError: # ValueError = 내장 예외 타입, int를 input받아야 하는데 int 외의 타입이 들어오면 ValueError이므로 except로 이동
        print("정수가 아닙니다. 다시 입력하세요.")

# 6의배수 부터 확인
if num ==0:
    print("0입니다.")
elif num%2==0 and num%3==0: #and연산자는 두 조건이 모두 참일때 True 반환
    print("6의 배수")
elif num%2==0:
    print("2의 배수")
elif num%3==0: 
    print("3의 배수")
else:
    print("해당 없음")