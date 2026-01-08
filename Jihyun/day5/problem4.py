# a = int(input("정수를 입력하세요:"))
# if (a%1) == 0:
#     result = a+10
# elif (a%1 !=0) or (a == 0):
#     result = a - 10
# printㅋ

a = int(input("정수를 입력하세요: "))
if a > 0:
    result = a +10
else:
    result = a - 10 
print(result)

# ====오답풀이 ====
# 1️⃣ 조건은 판별만 한다

# % 1 ❌ (의미 없음)

# a > 0 ⭕ (문제 조건 그대로)