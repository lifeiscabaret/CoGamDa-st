# ❓ 문제
# 아래 조건을 만족하는 프로그램을 작성하시오.
# 📋 조건
# 바깥 반복문은 i가 0부터 2까지 반복
# 안쪽 반복문은 j가 0부터 2까지 반복
# 단, j == 1일 때는 출력하지 않고 건너뛴다 (continue 사용)

# 🧾 출력 예시 (형식 자유)
# 0 0
# 0 2
# 1 0
# 1 2
# 2 0
# 2 2

# 💡 힌트
# if j == 1:
#     continue 

for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        
        print(i, j)
        
# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break
        
#         print(i, j)