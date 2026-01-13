# [week 2]

# 라벨과 키워드 (우선순위 고정)
labels = ["PAYMENT", "ACCOUNT", "BUG"]
keywords = [
    ["pay", "card", "refund", "price"],
    ["login", "password", "signup", "account"],
    ["error", "bug", "crash", "fail"]
]

# 1. N 유효성 검사(입력 조건: 1~20 사이의 정수만)
while True:
    n_input = input("문의 개수(N)를 입력하세요 (1~20): ")
    if n_input.isdigit():
        N = int(n_input)
        if 1 <= N <= 20:
            break
    print("올바른 범위의 숫자를 입력해주세요.")

# [결과 저장 및 통계용 변수 초기화]
results = []
# 처음에는 모두 0부터 시작하도록 설정 (컴퓨터는 존재하지 않는 칸에 숫자를 더할 수 없기 때문)
# 출력 예시와 같이 발견되지 않은 라벨도 0으로 출력하기 위함
counts = {label: 0 for label in labels + ["OTHER"]}

# 2. 데이터 전처리 및 라벨링 프로세스
print(f"{N}개의 문장을 입력하세요:")
for _ in range(N):
    sentence = input().strip()

    if not sentence:
        continue

    processed_sentence = sentence.lower()
    final_label = "OTHER" # 키워드를 못 찾을 경우를 대비한 기본 라벨 설정

    # 각 문장의 판정 결과가 다음 문장에 영향을 주지 않도록 매 반복(Loop)마다 플래그 리셋
    found = False

    # 우선순위 기반 라벨링
    for i in range(len(labels)):
        for key in keywords[i]:
            if key in processed_sentence:
                final_label = labels[i]
                found = True
                # 특정 라벨 내에서 키워드 발견 시 해당 라벨 내의 추가 탐색 중단
                break

        if found:
            # 상위 우선순위 라벨이 결정되면 하위 순위 라벨 검사를 즉시 종료
            # 문제 조건 중 '여러 키워드가 있어도 우선순위가 높은 라벨 1개만 적용'
            break

    # 결과 저장 및 라벨별 실시간 통계
    results.append(f"[{final_label}] {sentence}")
    counts[final_label] += 1
    # counts[final_label] += 1 이 부분 로직이 헷갈려서 직접 정리해봄..
    # 1. 라벨 확인 -> 2. 기존 데이터 조회 -> 3. 1 더하기 -> 4. 다시 저장
    # 이 과정이 N번 반복되면 마지막에는
    # 각 라벨에 해당하는 문장의 총 개수가 저장소에 쌓이게 된다.
    # 예를 들어 상세 내역(results)만 있으면 나중에
    # "그래서 결제 문의가 총 몇 건이야?"라고 물었을 때 처음부터 다시 세어야 하지만
    # 통계(counts)를 실시간으로 내두면
    # 마지막에 "결제 문의는 총 N건입니다"라고 답할 수 있게 된다.

# 3. 최종 결과 및 통계 출력
print("\n-- 처리 결과 --")
for res in results:
    print(res)

print(f"\nPAYMENT:{counts['PAYMENT']} ACCOUNT:{counts['ACCOUNT']} BUG:{counts['BUG']} OTHER:{counts['OTHER']}")


# 문의 개수(N)를 입력하세요 (1~20): 1
# 1개의 문장을 입력하세요:
# I forgot my PASSWORD

# -- 처리 결과 --
# [ACCOUNT] I forgot my PASSWORD

# PAYMENT:0 ACCOUNT:1 BUG:0 OTHER:0