'''
문제
FastAPI 서버의 요청 로그를 콘솔로 수집한다고 가정한다.
사용자로부터 반복해서 아래를 입력받는다.
API 경로 (/login, /users, /items/1 등)
응답 시간(ms)
STOP 입력 시 종료.
처리 조건
경로가 비어 있으면 "EMPTY PATH" 출력 후 재입력
응답 시간이 숫자가 아니면 "INVALID TIME"
0 미만이면 "NEGATIVE TIME"
유효한 로그만 저장
'''
# 변수 설정
max_time = -1 
# 왜 -1인가? 응답시간은 무조건 0이상일 것이기 때문에
# 유효 로그가 하나도 없을때를 표현하려면 -1이 적당하다.
slowest_path = ""

while True:
    path = input("API 경로를 입력하세요: ").strip()

    # 종료 조건
    if path == "STOP":
        break

    # 경로 검증
    if path == "":
        print("EMPTY PATH")
        continue # 경로 입력으로 돌아감

    # 응답 시간 입력 (중첩 루프)
    while True:
        time_input = input("응답 시간을 입력하세요(ms): ").strip()

        # 숫자 검증
        if not time_input.isdigit():
            print("INVALID TIME")
            continue

        response_time = int(time_input)

        # 음수 검증
        if response_time < 0:
            print("NEGATIVE TIME")
            continue

        # 유효한 응답 시간 → 중첩 루프 탈출
        break

    # 최댓값 갱신
    if response_time > max_time:
        max_time = response_time
        slowest_path = path

# 출력
if max_time == -1:
    print("NO LOGS")
else:
    print(f"SLOWEST: {slowest_path} ({max_time}ms)")
