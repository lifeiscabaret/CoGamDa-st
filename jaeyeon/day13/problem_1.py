'''
jaeyeon.day13.problem_1의 Docstring

[기초 문제 1] 배수 판별기
문제
정수 하나를 입력받아 다음 조건에 따라 출력하시오.
•	2와 3의 배수 → "6의 배수"
•	2의 배수 → "2의 배수"
•	3의 배수 → "3의 배수"
•	아무것도 아니면 → "해당 없음"
조건
•	if / elif / else 사용
•	조건 순서 중요
👉 포인트
•	나머지 연산자 %
•	조건 우선순위 사고

'''

num = int(input("정수입력: "))
if num % 6 == 0: 
    print("6의 배수")
elif num % 2 == 0:
    print("2의 배수")
elif num % 3 == 0:
    print("3의 배수")
else:
    print("해당 없음")
