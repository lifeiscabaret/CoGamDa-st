#문제
'''
사용자로부터 숫자 두 개를 입력받아
아래 네 가지 연산의 결과를 모두 출력하시오.
더하기
빼기
곱하기
나누기
'''

#풀이

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
 
print("더하기: ", num1 + num2)
print("빼기: ", num1 - num2)
print("곱하기: ", num1 * num2)
 
#0으로 나누기 방지
if num2 != 0:
    print("나누기: ", num1 / num2)
else:
    print("나누기: 0으로 나눌 수 없습니다.")