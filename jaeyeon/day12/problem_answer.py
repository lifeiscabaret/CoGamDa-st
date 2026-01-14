import re

# 입력부

pattern_response_time = r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$"
data_list = []  # logs [{path, time}, ...] 을 위한 빈리스트

cnt = 0
while True:
    ## api 경로 입력부
    input_path_str = input(f"{cnt + 1}번째 API경로 입력(stop 입력시 종료): ")
    input_path_str = input_path_str.strip()
    if input_path_str == "":
        print("EMPTY PATH")
        continue
    stop_word = input_path_str.lower()
    if stop_word == "stop":
        break
    cnt += 1
    ##################################
    ## 응답시간 입력부
    ## 단위는 ms, 즉 소수점자리 수도 입력받을 수 있되 정수로 변환
    while True:
        input_response_time = input("응답시간(정수) 입력: ")
        if not re.match(pattern_response_time, input_response_time):
            print("INVALID TIME")
            continue
        input_response_time = int(round(float(input_response_time)))
        if input_response_time < 0:
            print("NAGATIVE TIME")
            continue
        break
    # 내가 짰던 버전(3줄)
    data_dict = {}
    data_dict[input_path_str] = input_response_time
    data_list.append(data_dict)
    # 축약 버전 (1줄)
    # data_list.append({input_path_str: input_response_time})

# 출력부
if len(data_list) < 1:
    print("NO LOGS")
else:
    max_ms = 0
    path = ""
    for data_dict in data_list:
        for key, value in data_dict.items():
            if value >= max_ms:
                max_ms = value
                path = key

    print(f"SLOWEST: {path} ({max_ms}ms)")
