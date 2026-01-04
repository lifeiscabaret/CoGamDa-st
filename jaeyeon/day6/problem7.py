"""
[day6] 심화문제 1. 로그인 ID 미니 버전
사용자로부터 영문 이름을 입력받아

아래 조건에 맞는 ID를 생성하세요.
📌 조건
이름을 소문자로 변환
앞에서 최대 6글자만 사용
for문 한 번 이상 사용
📌 입력 예시
Jihyun
📤 출력 예시
jihyun
(랜덤 숫자는 아직 안 붙여도 됨 )
"""

# 풀이
user_id = input("영문이름 입력: ")
user_id = user_id.lower()[:6]
print(user_id)
