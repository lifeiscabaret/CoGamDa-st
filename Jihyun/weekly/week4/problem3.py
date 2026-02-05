# [심화 문제 1] 가장 느린 API 찾기

slowest_path = ""
slowest_time = None  # 아직 유효 로그가 없다는 뜻

while True:
    path = input("API 경로 입력 (STOP 종료): ").strip()

    if path == "STOP":
        break

    if path == "":
        print("EMPTY PATH")
        continue  # 경로 다시 받으러 위로

    # 응답시간은 "유효할 때까지" 계속 입력받아야 하니까 중첩 루프
    while True:
        time_str = input("응답 시간(ms) 입력: ").strip()

        # 숫자인지 검사 (음수는 일단 숫자 변환까지는 되니까 여기선 제외)
        try:
            time_ms = int(time_str)
        except ValueError:
            print("INVALID TIME")
            continue  # 응답시간 다시 입력

        if time_ms < 0:
            print("NEGATIVE TIME")
            continue  # 응답시간 다시 입력

        # 여기까지 왔으면 응답시간이 유효함 -> 중첩루프 탈출
        break

    # 유효 로그 저장(최대값 갱신)
    if slowest_time is None or time_ms > slowest_time:
        slowest_time = time_ms
        slowest_path = path

# 출력
if slowest_time is None:
    print("NO LOGS")
else:
    print(f"SLOWEST: {slowest_path} ({slowest_time}ms)")
