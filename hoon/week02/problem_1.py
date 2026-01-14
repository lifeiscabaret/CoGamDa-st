#문제
'''
고객 문의 문장들을 전처리한 뒤, 키워드 포함 여부로 라벨을 붙여 출력하라.
라벨과 키워드(우선순위 고정):
PAYMENT: pay, card, refund, price
ACCOUNT: login, password, signup, account
BUG: error, bug, crash, fail
그 외: OTHER
라벨은 PAYMENT → ACCOUNT → BUG → OTHER 순서로 판정한다.
(여러 키워드가 있어도 우선순위가 높은 라벨 1개만 적용)
'''

#풀이

while True:
    n = input()

    if not n:
        continue

    if not n.isdigit(): #??? 이해 ok, 다른 방법?
        continue

    N = int(n)
    if 1 <= N <= 20:
        break

categories = [
    ("PAYMENT", ["pay", "card", "refund", "price"]),
    ("ACCOUNT", ["login", "password", "signup", "account"]),
    ("BUG", ["error", "bug", "crash", "fail"])
]

cnt_payment = 0
cnt_account = 0
cnt_bug = 0
cnt_other = 0

results = []

for _ in range(N):
    text = input()
    text = text.strip()
    
    if not text:
        continue

    lower_text = text.lower()

    label = "OTHER"
    found = False

    for category_name, keywords in categories:
        for key in keywords:    #내부 for문 어려움
            if key in lower_text:
                label = category_name
                found = True
                break
        
        if found:
            break
    
    if label == "PAYMENT":
        cnt_payment +=1
    elif label == "ACCOUNT":
        cnt_account +=1
    elif label == "BUG":
        cnt_bug +=1
    else:
        cnt_other += 1
    
    results.append(f"[{label}] {lower_text}")

for r in results:
    print(r)

print(f"PAYMENT:{cnt_payment} ACCOUNT:{cnt_account} BUG:{cnt_bug} OTHER:{cnt_other}")

#??? 원하는 결과 느낌 아님, 못찾겠음



# 효율적인 코드 (셀프스터디용)
# try문 잘 쓰이지 않음
'''
import sys
from collections import Counter

def get_valid_n():
    """1~20 사이의 정수 N을 입력받을 때까지 반복하는 함수"""
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                continue
            n = int(line)
            if 1 <= n <= 20:
                return n
        except ValueError:
            continue # 숫자가 아니면 무시하고 재시도

def solve():
    # 1. 입력 받기
    N = get_valid_n()

    # 2. 우선순위 및 키워드 설정 (순서 보장을 위해 튜플 리스트 사용)
    # 딕셔너리는 3.7+부터 순서가 보장되지만, 명시적인 우선순위 로직엔 리스트가 안전함
    priorities = [
        ("PAYMENT", {"pay", "card", "refund", "price"}), # 검색 속도를 위해 set 사용
        ("ACCOUNT", {"login", "password", "signup", "account"}),
        ("BUG",     {"error", "bug", "crash", "fail"})
    ]

    results = []
    # Counter는 키가 없으면 0을 반환하므로 초기화 걱정이 없음
    counts = Counter() 

    # 3. 문장 처리
    for _ in range(N):
        text = sys.stdin.readline().strip()
        
        if not text:
            continue

        lower_text = text.lower()
        assigned_label = "OTHER"

        # 우선순위대로 검사
        for label, keywords in priorities:
            # any(): 키워드 중 하나라도 포함되어 있으면 True (효율적)
            if any(keyword in lower_text for keyword in keywords):
                assigned_label = label
                break # 상위 우선순위 발견 시 즉시 종료
        
        counts[assigned_label] += 1
        results.append(f"[{assigned_label}] {lower_text}")

    # 4. 결과 출력
    print('\n'.join(results))
    
    # 통계 출력 (순서 고정)
    stat_order = ["PAYMENT", "ACCOUNT", "BUG", "OTHER"]
    stat_str = " ".join([f"{label}:{counts[label]}" for label in stat_order])
    print(stat_str)

if __name__ == "__main__":
    solve()
'''