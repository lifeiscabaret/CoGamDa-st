'''
jaeyeon.day13.problem_3의 Docstring

[심화 문제 1] 가장 느린 API 찾기 
문제
FastAPI 서버의 요청 로그를 콘솔로 수집한다고 가정한다.
사용자로부터 반복해서 아래를 입력받는다.
1.	API 경로 (/login, /users, /items/1 등)
2.	응답 시간(ms)
STOP 입력 시 종료.
________________________________________
처리 조건
•	경로가 비어 있으면 "EMPTY PATH" 출력 후 재입력
•	응답 시간이 숫자가 아니면 "INVALID TIME"
•	0 미만이면 "NEGATIVE TIME"
•	유효한 로그만 저장
________________________________________
출력
•	가장 응답 시간이 오래 걸린 API와 시간
SLOWEST: /login (320ms)
•	유효 로그가 하나도 없으면
NO LOGS
________________________________________
구현 요구
•	while True
•	중첩 루프 (응답시간 유효할 때까지)
•	continue, break
•	최댓값 갱신 시 경로도 함께 저장
👉 포인트
•	실무 로그 분석 사고
•	“값 + 맥락 정보” 같이 관리
•	week3 웹 문제와 자연스럽게 연결됨

'''

server_response_time = 0
user_input_response_time_lower = ""
vaild_log_list = []

while True:
    user_input_api_path = input("API 경로: ")
    user_input_api_path_lower = user_input_api_path.lower()
    if user_input_api_path == "":
        print("EMPTY PATH")
        continue
    if user_input_api_path_lower == "stop":
        print("종료")
        break
    while True:
        user_input_response_time = input("응답 시간(ms): ")
        user_input_response_time_lower = user_input_response_time.lower()
        if user_input_response_time_lower == "stop":
            print("종료")
            exit()
        try:
            user_input_response_time_lower_int = int(user_input_response_time_lower)
            if user_input_response_time_lower_int < 0:
                print("NEGATIVE TIME")
                continue
            else:
                server_response_time = user_input_response_time_lower_int
                valid_log_dict = { "path" : user_input_api_path, "time" : user_input_response_time_lower_int}
                vaild_log_list.append(valid_log_dict)
                break
        except ValueError:
            print("INVALID TIME")

if vaild_log_list:
    max_log = vaild_log_list[0]
    for log in vaild_log_list[1:]:
        if log["time"] > max_log["time"]:
            max_log = log
    print(f"SLOWEST: {max_log['path']} ({max_log['time']}ms)")
else:
    print("NO LOGS")

# if vaild_log_list:
#     max_log = max(vaild_log_list, key=lambda x: x["time"])
#     print(f"SLOWEST: {max_log['path']} ({max_log['time']}ms)")
# else:
#     print("NO LOGS")