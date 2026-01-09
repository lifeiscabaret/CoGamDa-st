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

# 전체적으로 필요 없던 파츠들과 중복 파츠들을 삭제하여 간결화 하였습니다.

############### 1. 데이터셋 #####################################################################
# 리스트를 활용해 필터 단어들을 설정합니다.
PAYMENT = ["pay", "card", "refund", "price"]
ACCOUNT = ["login", "password", "signup", "account"]
BUG = ["error", "bug", "crash", "fail"]

############### 2. 사용자입력부 #################################################################
# 문장개수 설정부입니다. 입력받은 정수를 line_num 변수에 저장해 문장입력부의 반복횟수를 결정합니다.
while True:
    try:  # 입력값 양식제한 적용
        line_num = int(input("정수입력(1~20) : "))
        if 1 <= line_num <= 20:  # 입력값 숫자범위제한 적용
            break
        else:
            print("범위에 맞게 다시 입력하세요")
    except ValueError:
        print("양식에 맞게 다시 입력하세요")

# 문장입력부입니다. 입력한 문장을 line_list 리스트에 요소로 추가합니다.
i = 1
line_list = []
while True:
    line = input(f"{i}번째 문장입력: ")
    line_list.append(line)
    i += 1
    if i > line_num:
        break

############### 3. 입력데이터전처리 및 통계처리 ###################################################
# 변수 선언 및 초기화 구간
line_list_lower = []
new_line_list = []
cnt_payment = cnt_account = cnt_bug = cnt_other = (
    0  # 변수에 공통된 값을 대입할 때는 한 줄로 처리가능합니다. 통계처리에 사용할 변수들의 초기화
)
marker = ""  # 문제의 요구사항대로 문장별 라벨을 붙일 때 사용할 변수 '마커'입니다.

# 소문자 변환 구간
for line in line_list:
    line = line.lower()
    line_list_lower.append(
        line
    )  # 스그모임때 깜빡하고 적용하지 않았던 소문자처리 부분입니다. 변환된 소문자문장은 line_list_lower 리스트에 저장됩니다.

# 라벨링 구간
# 개인적인 개선사항으로 단어별 라벨링 요소를 추가하였습니다.
for line in line_list_lower:
    for word in PAYMENT:
        if word in line:
            line = line.replace(
                word, f"[PAYMENT]{word}"
            )  # replace함수로 단어별 라벨을 적용합니다.
            cnt_payment += 1  # 통계처리가 작동합니다
    for word in ACCOUNT:
        if word in line:
            line = line.replace(
                word, f"[ACCOUNT]{word}"
            )  # replace함수로 단어별 라벨을 적용합니다.
            cnt_account += 1  # 통계처리가 작동합니다
    for word in BUG:
        if word in line:
            line = line.replace(
                word, f"[BUG]{word}"
            )  # replace함수로 단어별 라벨을 적용합니다.
            cnt_bug += 1  # 통계처리가 작동합니다

    # 문제에서 요구한 우선순위에 따른 문장별 라벨링 적용구간입니다.
    if "[PAYMENT]" in line:
        marker = "[PAYMENT]"
    elif "[ACCOUNT]" in line:
        marker = "[ACCOUNT]"
    elif "[BUG]" in line:
        marker = "[BUG]"
    else:
        marker = "[OTHER]"  # 문장 안에 기설정된 라벨이 모두 없을 경우 [OTHER] 마커를 붙여 라벨링합니다
        cnt_other += 1  # 통계처리가 작동합니다.
    line = marker + " : " + line  # 최종출력에 사용할 문장이 line 변수에 저장됩니다.
    new_line_list.append(
        line
    )  # 수정본출력에 사용할 리스트의 요소추가기능이 작동합니다.


############### 4. 출력부 #####################################################################
print("--원본출력--")
for line in line_list:
    print(line)
print("--수정본출력---")
for line in new_line_list:
    print(line)
print(
    "--레이블통계--"
)  # 통계 결과는 개인적으로 적용한 단어별 라벨링 기능으로 인해 예시문제의 답안과 차이가 있을것입니다.
print(
    f"PAYMENT:{cnt_payment} ACCOUNT:{cnt_account} BUG:{cnt_bug} OTHER:{cnt_other}"
)  # 라벨링된 단어별 통계출력
