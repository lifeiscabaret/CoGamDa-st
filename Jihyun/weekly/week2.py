labels = [
    ("PAYMENT", ["pay", "card", "refund", "price"]),
    ("ACCOUNT", ["login", "password", "signup", "account"]),
    ("BUG", ["error", "bug", "crash", "fail"]),
]

# 1) N 유효성 검사: while True + break
while True:
    try:
        N = int(input("문의하실 건수를 입력하세요(숫자만)").strip())
        if 1 <= N <= 20:
            break
    except:
        pass  # 숫자 변환 실패도 다시 입력받기

# 결과 저장용 리스트
processed = []

# 라벨 카운트 딕셔너리(또는 리스트)
counts = {"PAYMENT": 0, "ACCOUNT": 0, "BUG": 0, "OTHER": 0}

# 2) N개 문장 입력 받기
for _ in range(N):
    sentence = input("문의사항(영어로): ").strip()   # 양쪽 공백 제거

    # 비어 있으면 무시(스킵): continue
    if sentence == "":
        continue

    sentence = sentence.lower()  # 소문자 변환(전처리)

    # 3) 라벨 판정 (우선순위: PAYMENT -> ACCOUNT -> BUG -> OTHER)
    label = "OTHER"

    # 중첩 반복문: 라벨/키워드 탐색
    for lab, keywords in labels:
        for kw in keywords:
            if kw in sentence:
                label = lab
                break            # 키워드 찾으면 내부 루프 종료
        if label != "OTHER":
            break                # 라벨 확정되면 바깥 루프도 종료

    # 저장 + 카운트
    processed.append((label, sentence))
    counts[label] += 1

# 4) 출력
for lab, sent in processed:
    print(f"[{lab}] {sent}")

print(f"PAYMENT:{counts['PAYMENT']} ACCOUNT:{counts['ACCOUNT']} BUG:{counts['BUG']} OTHER:{counts['OTHER']}")

'''
문의하실 건수를 입력하세요(숫자만): 1
i want refund
[PAYMENT] i want refund
PAYMENT:1 ACCOUNT:0 BUG:0 OTHER:0
'''