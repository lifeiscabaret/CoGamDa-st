# 문제
# 고객 문의 문장들을 전처리한 뒤, 키워드 포함 여부로 라벨을 붙여 출력하라.
# 라벨과 키워드(우선순위 고정):
# - PAYMENT: pay, card, refund, price
# - ACCOUNT: login, password, signup, account
# - BUG: error, bug, crash, fail
# - 그 외: OTHER

# 라벨은 PAYMENT → ACCOUNT → BUG → OTHER 순서로 판정한다.
# (여러 키워드가 있어도 우선순위가 높은 라벨 1개만 적용)
 
# 입력
# - 첫 줄: 정수 N
# - 다음 줄부터: 문의 문장 N개 (한 줄 1문장)

# 입력 조건
# - 1 ≤ N ≤ 20
# - 범위를 벗어나면 올바른 값이 들어올 때까지 다시 입력받는다.

# 전처리
# 각 문장에 대해:
# 1. 양쪽 공백 제거(strip)
# 2. 비어 있으면 무시
# 3. 소문자 변환 후 라벨 판정

# 출력

# 전처리 후 남은 문장들을 입력 순서대로 출력:
# - [{LABEL}] {sentence}

# 마지막 줄에 라벨별 개수 출력:
# - PAYMENT:x ACCOUNT:y BUG:z OTHER:w

# 구현 요구(필수)
# - while True + break: N 유효성 검사
# - continue: 빈 문장 스킵
# - 중첩 반복문으로 라벨/키워드 탐색
# - 라벨 확정 시 break
# - 리스트 사용

# 예시 입력
# 5
# I want a REFUND please
# Login FAIL when I try
# The app CRASH on start 
# Where is the nearest store?

# 예시 출력
# [PAYMENT] i want a refund please
# [ACCOUNT] login fail when i try[BUG] the app crash on start
# [OTHER] where is the nearest store?
# PAYMENT:1 ACCOUNT:1 BUG:1 OTHER:1

# keyword_by_label = {
#     "PAYMENT": ["pay", "card", "refund", "price"], 
#     "ACCOUNT": ["login", "password", "signup", "account"],
#     "BUG": ["error", "bug", "crash", "fail"],
#     "OTHER": []    
# }

# N = int(input("정수를 입력하세요:"))
# sentences = []

# while True:
#     if  1 <= N <= 20:
#         break
# else:
#     input("다시 입력하세요:")
    
# for s in sentences:
#     s = s.strip().lower()
    
# results = keyword_by_label

# found_label = "OTHER" # 기본값 설정

# for label, keywords in results.items():
#     # 1. 키워드 리스트를 하나씩 확인하는 루프를 하나 더 만들거나,
#     # 2. 'any()' 함수를 써서 문장 안에 키워드가 있는지 확인
#     if keywords in sentences:
#         found_label = label
#         break # 찾았으면 우선순위에 따라 멈춤!

# # 루프가 다 끝난 '뒤에' 최종 결정된 found_label 과 문장을 출력
# print(f"[{keyword_by_label}] {sentences}")

keyword_by_label = {
    "PAYMENT": ["pay", "card", "refund", "price"], 
    "ACCOUNT": ["login", "password", "signup", "account"],
    "BUG": ["error", "bug", "crash", "fail"],
    "OTHER": []    
}

# 1. N을 입력받는 while 루프(지금 코드에서 input 을 N 에 다시 담아줘야 함!)
while True:
    # ... 여기서 N 을 다시 입력받는 로직 필요
    N = int(input("정수를 입력하세요:"))
    if 1 <= N <= 20:
        break
        # 올바른 범위라면? 여기서 무한 루프를 끝냅니다.
    else:
        # 범위를 벗어났다면? 안내 메시지를 출력합니다.
        # 따로 명령하지 않아도 while 문의 처음으로 돌아가 다시 입력을 받게 됩니다.
        print(input("1에서 20 사이의 숫자를 입력해 주세요:"))

final_results = []
counts = {"PAYMENT": 0, "ACCOUNT": 0, "BUG": 0, "OTHER": 0}

# 2. 문장을 하나씩 처리하는 메인 루프
for i in range(N):
    raw_s = input() # 여기서 문장을 직접 입력받습니다.
    s = raw_s.strip().lower() # 즉시 전처리
    
    if not s: # 비어있으면 무시
        continue
    
    found_label = "OTHER"
    
    # 3. 라벨 판정 로프(이 안에서 s 와 키워드를 비교)
    for label, keywords in keyword_by_label.items():
        if label == "OTHER": continue
        
        # 힌트 'any'를 써서 keywords 중 하나라도 s 에 있는지 확인!
        if any(word in s for word in keywords):
            found_label = label
            break
    
    counts[found_label] += 1
    
    # 4. 판정 직후 바로 출력
    print(f"[{found_label}] {s}")
    print(counts[found_label])