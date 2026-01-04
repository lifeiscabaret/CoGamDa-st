"""
[day6]응용문제 2. 숫자 누적 합
1부터 10까지의 합을 구해서 출력하세요.
📤 출력 예시
합계: 55
"""

# 풀이
total = 0
for i in range(1, 11):
    total += i
print(total)
