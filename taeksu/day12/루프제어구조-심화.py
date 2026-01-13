# 1차 시도
# path = input("API 경로를 입력하세요:")
# time = int(input("응답시간(ms)을 입력하세요:"))

# if path in ["STOP", "stop", "Stop"]:
#     print("입력 종료")
# else:
#     raw_s = input()
#     s = raw_s.strip()
#     if s == input(" "):
#         print("EMPTY PATH")
#     continue

# 2차 시도
# while True:
#     path = input("API 경로를 입력하세요: ").strip()

#     if path.lower() == "stop":
#         print("입력 종료")
#         break

#     if not path:
#         print("EMPTY PATH")
#         continue

#     time_ms = int(input("응답시간(ms)을 입력하세요: "))
    
# 3차 시도
# empty_list = []

# while True:
#     path = input("API 경로를 입력하세요:")
#     path = path.strip()
#     if path in ["STOP", "Stop", "stop"]:
#         print("입력 종료")
#         break
#     elif path == "":
#         print("EMPTY PATH")
#         continue
#     while True:
#         try:
#             time = int(input("응답시간(ms)을 입력하세요:"))
#             if time < 0:
#                 "INVALID TIME"
#             else:
#                 "NEGATIVE TIME"                
#         except ValueError: # Exception 대신 ValueError를 쓰면 더 정확!:
#             print("숫자를 입력하세요:")
#             break
            
# max_time = -1
# slowest_path = ??

# empty_list.append((path, time))

# 4차 시도
empty_list = []

while True:
    path = input("API 경로를 입력하세요:")
    path = path.strip()
    # if path in ["STOP", "Stop", "stop"]:
    if path.upper() == "STOP":
        print("입력 종료")
        break
    elif path == "":
        print("EMPTY PATH")
        continue
    while True:
        try:
            time = int(input("응답시간(ms)을 입력하세요:"))
        except ValueError: # Exception 대신 ValueError를 쓰면 더 정확!:
            print("INVALID TIME")
            continue
        
        if time < 0:
            print("NEGATIVE TIME")
            continue
        else:
            print(time)                
        
            empty_list.append((path, time))
            break

if not empty_list:
    # 텅 비었을 때 처리
    print("NO LOGS")
else:
    # 데이터가 있을 때만 최댓값 계산 시작            
    max_time = -1
    slowest_path = None

    for p, t in empty_list:
        if t > max_time:
            max_time = t
            slowest_path = p

    # 마지막 결과 출력        
    print(f"SLOWEST: {slowest_path} ({max_time}ms)")