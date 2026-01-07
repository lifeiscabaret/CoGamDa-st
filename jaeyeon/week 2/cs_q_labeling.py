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
