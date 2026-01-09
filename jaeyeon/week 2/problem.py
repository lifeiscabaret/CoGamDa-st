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
[ACCOUNT] login fail when i try
[BUG] the app crash on start
[OTHER] where is the nearest store?
PAYMENT:1 ACCOUNT:1 BUG:1 OTHER:1

"""

PAYMENT = ["pay", "card", "refund", "price"]
ACCOUNT = ["login", "password", "signup", "account"]
BUG = ["error", "bug", "crash", "fail"]
OTHER = []
LABLE = [PAYMENT, ACCOUNT, BUG, OTHER]

while True:
    try:
        line_num = int(input("정수입력(1~20) : "))
        if 1 <= line_num <= 20:
            break
        else:
            print("범위에 맞게 다시 입력하세요")
    except ValueError:
        print("양식에 맞게 다시 입력하세요")

i = 1
line_list = []
while True:
    line = input(f"{i}번째 문장입력: ")
    line_list.append(line)
    i += 1
    if i > line_num:
        break

new_line_list = []
cnt_payment = 0
cnt_account = 0
cnt_bug = 0
cnt_other = 0
marker = ""
for line in line_list:
    for word in PAYMENT:
        if word in line:
            new_line = line.replace(word, f"[PAYMENT]{word}")
            line = new_line
            cnt_payment += 1
    for word in ACCOUNT:
        if word in line:
            new_line = line.replace(word, f"[ACCOUNT]{word}")
            line = new_line
            cnt_account += 1
    for word in BUG:
        if word in line:
            new_line = line.replace(word, f"[BUG]{word}")
            line = new_line
            cnt_bug += 1
    if "[PAYMENT]" in line:
        marker = "[PAYMENT]"
    elif "[ACCOUNT]" in line:
        marker = "[ACCOUNT]"
    elif "[BUG]" in line:
        marker = "[BUG]"
    else:
        marker = "[OTHER]"
        cnt_other += 1
    line = marker + " : " + line
    new_line_list.append(line)

change_rule = dict(zip(line_list, new_line_list))
changed_line_list = []
for line in line_list:
    if line in change_rule:
        changed_line_list.append(change_rule[line])
    else:
        changed_line_list.append(line)

print("--원본출력--")
for line in line_list:
    print(line)
print("--수정본출력---")
for line in changed_line_list:
    print(line)
print("--레이블통계--")
print(f"PAYMENT:{cnt_payment} ACCOUNT:{cnt_account} BUG:{cnt_bug} OTHER:{cnt_other}")
