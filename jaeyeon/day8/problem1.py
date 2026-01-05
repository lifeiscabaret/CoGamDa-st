"""
[day8]문제 1. while 흐름 이해하기
문제
다음 코드의 출력 결과를 순서대로 쓰시오.
n = 0
while n < 5:
    if n == 3:
        break
    print(n)
    n += 1
체크 포인트
•	while 조건은 언제까지 True인가? n이 3일 때까지
•	break는 언제 실행되는가? n이 3일 때
•	print(n)은 몇 번 실행되는가? 3번
⚠️ 코드 수정 ❌ / 결과만 쓰기
"""

# 풀이
"""
n | While 조건식 | if 조건식 | 터미널 출력
0 | True | False | 0
1 | True | False | 1
2 | True | False | 2
3 | True | True(break) | -
-
"""
"""
예제 구문에서 print(n)의 들여쓰기가 while문의 시작과 동축상에 놓이면
IndentationError: unindent does not match any outer indentation level
에러가 발생함
"""
