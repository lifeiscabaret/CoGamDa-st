#CS 문의 라벨링 전처리

'''
문제
고객 문의 문장들을 전처리한 뒤, 키워드 포함 여부로 라벨을 붙여 출력하라.
라벨과 키워드(우선순위 고정):
●PAYMENT: pay, card, refund, price
●ACCOUNT: login, password, signup, account
●BUG: error, bug, crash, fail
●그 외: OTHER
라벨은 PAYMENT → ACCOUNT → BUG → OTHER 순서로 판정한다.
(여러 키워드가 있어도 우선순위가 높은 라벨 1개만 적용)
 
입력
●첫 줄: 정수 N
●다음 줄부터: 문의 문장 N개 (한 줄 1문장)

입력 조건
●1 ≤ N ≤ 20
●범위를 벗어나면 올바른 값이 들어올 때까지 다시 입력받는다.

전처리
각 문장에 대해:
●양쪽 공백 제거(strip)
●비어 있으면 무시
●소문자 변환 후 라벨 판정

출력
전처리 후 남은 문장들을 입력 순서대로 출력:
●[{LABEL}] {sentence}

마지막 줄에 라벨별 개수 출력:
●PAYMENT:x ACCOUNT:y BUG:z OTHER:w

구현 요구(필수)
●while True + break: N 유효성 검사
●continue: 빈 문장 스킵
●중첩 반복문으로 라벨/키워드 탐색
●라벨 확정 시 break
●리스트 사용
'''

'''
#문제풀이 접근
일단 입력받은 N이 유효한지 검사하는 while문을 작성한다.
그 다음 N개의 문장을 입력받아 전처리(양쪽 공백 제거, 소문자 변환)를 수행.
빈 문장은 continue로 건너뛴다.
전처리 된 문장들을 if문과 중첩 반복문을 사용하여 키워드에 따라 라벨링.
각 라벨을 변수화 하여 개수를 세어 출력.
'''

# 문장 입력 받기
sentences_count = int(input("작성할 문장의 수: "))
sentences_list = []
# n 조건 검사
# n이 20이하라면 n번 문장 입력 받아서 문장 리스트에 추가
while True:
    if 1 <= sentences_count <= 20:
        for i in range(sentences_count):
            sentences = (input("문장을 입력하세요: "))
            #미리 전처리를 해서 넣어버리자
            sentences = sentences.strip()
            if sentences == "":
                continue
            sentences = sentences.lower()
            #전처리된 문장 리스트에 추가
            sentences_list.append(sentences)
    # n이 조건 불만족하면 다시 입력 받기
    else:
        print("1에서 20사이의 값을 입력하세요.")
        sentences_count = int(input("작성할 문장의 수: "))
        continue
    break

#확인용 출력
print(sentences_list)

#라벨링
payment_keywords = ['pay', 'card', 'refund', 'price']
account_keywords = ['login', 'password', 'signup', 'account']
bug_keywords = ['error', 'bug', 'crash', 'fail']
payment_conunt = 0
account_count = 0
bug_count = 0
other_count = 0

#라벨링된 키워드와 입력받은 문장 비교

for sentence in sentences_list: # 문장 리스트에서 문장 하나씩 가져오기
    label = "OTHER" # 기본 라벨 설정
    # PAYMENT 라벨링
    for keyword in payment_keywords: # 라벨 리스트에서 값을 하나씩 가져와서
        if keyword in sentence: # 문장에 포함되어 있는지 확인
            label = "PAYMENT" # 포함되어 있다면 라벨 변경
            payment_conunt += 1
            break
    # ACCOUNT 라벨링
    if label == "OTHER":
        for keyword in account_keywords:
            if keyword in sentence:
                label = "ACCOUNT"
                account_count += 1
                break
    # BUG 라벨링
    if label == "OTHER":
        for keyword in bug_keywords:
            if keyword in sentence:
                label = "BUG"
                bug_count += 1
                break
    # OTHER 라벨링
    if label == "OTHER": # 모든 라벨에 해당하지 않는다면
        other_count += 1

    # 라벨과 문장 출력
    print(f"[{label}] {sentence}")

# 라벨별 개수 출력
print(f"PAYMENT:{payment_conunt} ACCOUNT:{account_count} BUG:{bug_count} OTHER:{other_count}")