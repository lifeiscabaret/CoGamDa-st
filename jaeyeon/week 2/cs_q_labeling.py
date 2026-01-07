"""
[week 2] CS 문의 라벨링 전처리
문제
고객 문의 문장들을 전처리한 뒤, 키워드 포함 여부로 라벨을 붙여 출력하라.
라벨과 키워드(우선순위 고정):
•	PAYMENT: pay, card, refund, price
•	ACCOUNT: login, password, signup, account
•	BUG: error, bug, crash, fail
•	그 외: OTHER
라벨은 PAYMENT → ACCOUNT → BUG → OTHER 순서로 판정한다.
(여러 키워드가 있어도 우선순위가 높은 라벨 1개만 적용)

입력
•	첫 줄: 정수 N
•	다음 줄부터: 문의 문장 N개 (한 줄 1문장)
입력 조건
•	1 ≤ N ≤ 20
•	범위를 벗어나면 올바른 값이 들어올 때까지 다시 입력받는다.
전처리
각 문장에 대해:
1.	양쪽 공백 제거(strip)
2.	비어 있으면 무시
3.	소문자 변환 후 라벨 판정
출력
전처리 후 남은 문장들을 입력 순서대로 출력:
•	[{LABEL}] {sentence}
마지막 줄에 라벨별 개수 출력:
•	PAYMENT:x ACCOUNT:y BUG:z OTHER:w
구현 요구(필수)
•	while True + break: N 유효성 검사
•	continue: 빈 문장 스킵
•	중첩 반복문으로 라벨/키워드 탐색
•	라벨 확정 시 break
•	리스트 사용
예시 입력
5
I want a REFUND please

Login FAIL when I try
The app CRASH on start
Where is the nearest store?
예시 출력
[PAYMENT] i want a refund please
[ACCOUNT] login fail when i try[BUG] the app crash on start
[OTHER] where is the nearest store?
PAYMENT:1 ACCOUNT:1 BUG:1 OTHER:1

"""

import pandas as pd

PAYMENT = ["pay", "card", "refund", "price"]
ACCOUNT = ["login", "password", "signup", "account"]
BUG = ["error", "bug", "crash", "fail"]
OTHER = []

# 각 리스트를 Series로 변환하여 딕셔너리로 묶기
data = {
    "PAYMENT": pd.Series(PAYMENT),
    "ACCOUNT": pd.Series(ACCOUNT),
    "BUG": pd.Series(BUG),
    "OTHER": pd.Series(OTHER),
}

prio_label = pd.DataFrame(data)
print(prio_label)
print(prio_label.columns)

"""
# 컬럼 순서대로 우선순위를 적용하는 예시 로직
for column in prio_label.columns:
    # 해당 컬럼(우선순위 높은 순)의 단어들이 질문에 포함되어 있는지 체크
    # ... 로직 구현 ...
"""
cs_q_str = []

# 입력
while True:
    try:
        num_lines = int(input("정수 입력(1~20): "))
        if num_lines in range(1, 21):
            break
    except ValueError:
        print("다시 입력하세요")

for i in range(num_lines):
    line = input(f"{i + 1}번째 줄 입력: ")
    if line == "":
        cs_q_str.append("")
        continue
    cs_q_str.append(line)

# 전처리
pr_prcsd = []
for i in range(len(cs_q_str)):
    sentence = cs_q_str[i].strip().lower()
    if sentence != "":
        pr_prcsd.append(sentence)

lbl_sntc = []
keyword = []
for dfrow in range(4):
    for dfcol in range(4):
        lbl_sntc.append({dfrow: prio_label.iloc[dfcol, dfrow]})

for k in lbl_sntc:
    print(k)

# 출력
# for i in range(len(cs_q_str)):
#     print(cs_q_str[i])
# print("=" * 18)
# for i in range(len(pr_prcsd)):
#     print(pr_prcsd[i])

####################################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
###########################################################################
## Gemini
###########################################################################
"""
# 
import pandas as pd

PAYMENT = ["pay", "card", "refund", "price"]
ACCOUNT = ["login", "password", "signup", "account"]
BUG = ["error", "bug", "crash", "fail"]
OTHER = []

# 각 리스트를 Series로 변환하여 딕셔너리로 묶기
data = {
    "PAYMENT": pd.Series(PAYMENT),
    "ACCOUNT": pd.Series(ACCOUNT),
    "BUG": pd.Series(BUG),
    "OTHER": pd.Series(OTHER),
}

prio_label = pd.DataFrame(data)
print(prio_label)


# 
cs_q_list = []

# 1. N 유효성 검사
while True:
    try:
        num_lines = int(input("문장 개수 입력(1~20): "))
        if 1 <= num_lines <= 20:
            break
        print("1~20 사이의 정수를 입력하세요.")
    except ValueError:
        print("숫자만 입력 가능합니다.")

# 2. 문장 입력 (빈 줄 포함)
for i in range(num_lines):
    line = input(f"{i + 1}번째 줄 입력: ")

    if line.strip() == "":
        # 빈 문장일 때의 조건 처리
        cs_q_list.append("")  # 빈 칸으로 자리를 차지하게 함
        continue  # 아래 로직(있다면)을 실행하지 않고 다음 i로 넘어감

    cs_q_list.append(line)

# 전처리
pr_prcsd = [s for item in cs_q_str if (s := item.strip().lower()) != ""]
for sentence in pr_prcsd:
    for word in PAYMENT:
        if word in sentence: # 여기서 in 연산자 사용!
            print(f"문장: '{sentence}' -> 라벨: PAYMENT")
            break # 우선순위에 따라 하나 찾으면 중단

for sentence in pr_prcsd:
    assigned_label = "OTHER" # 기본값 설정
    
    # 1. 컬럼 순서대로 (왼쪽부터) 검사 시작
    for category in prio_label.columns:
        if category == "OTHER": continue
            
        # 2. 해당 카테고리의 단어 리스트를 가져와서 검사
        keywords = data[category].dropna() # NaN 제거한 단어들
        if any(word in sentence for word in keywords): # 파이썬의 리스트 컴프리헨션과 any() 함수가 결합된 아주 강력한 형태
            assigned_label = category
            break # 찾았으면 즉시 중단 (이게 바로 우선순위 구현!)
            
    print(f"문장: {sentence} -> 확정 라벨: {assigned_label}")                        

# 3. 출력 (메모장처럼 그대로 출력)
print("\n--- 출력 결과 ---")
for sentence in cs_q_list:
    print(sentence)
"""
