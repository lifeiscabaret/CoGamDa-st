"""
[day9]응용 문제 1.(break / continue 실전 적용)
❓ 문제
아래 조건을 만족하는 프로그램을 작성하시오.
📋 조건
•	바깥 반복문은 i가 0부터 2까지 반복
•	안쪽 반복문은 j가 0부터 2까지 반복
•	단, j == 1일 때는 출력하지 않고 건너뛴다 (continue 사용)
🧾 출력 예시 (형식 자유)
0 0
0 2
1 0
1 2
2 0
2 2
💡 힌트
if j == 1:
    continue
📌 문제 포인트
•	continue는 현재 반복만 스킵
•	중첩 루프 안에서 continue가 어디까지 영향을 주는지 이해하기
"""
# 풀이

for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
