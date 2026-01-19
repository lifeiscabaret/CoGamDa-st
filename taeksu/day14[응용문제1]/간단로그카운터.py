# [응용 문제 1] 간단 로그 카운터
# 문제
# 다음과 같은 로그 레벨이 있다.
# "INFO"
# "WARN"
# "ERROR"
# 사용자로부터 로그 레벨을 여러 번 입력받아,

# 각 레벨이 몇 번 나왔는지 출력하시오.
# "STOP" 입력 시 종료
# 대소문자 구분 없음
# 👉 출력 예
# INFO: 3 WARN: 1 ERROR: 2 
# 👉 포인트
# 딕셔너리 카운트
# 문자열 전처리
# 루프 종료 조건

# 1차 시도
# counts = {"INFO_list":0, "WARN_list":0, "ERROR_list":0}

# while True:
#     log = input("로그 레벨 입력: ").upper()
#     if log == "STOP":
#         break
#     elif log == "INFO_list":
#         "INFO_list" += 1
#     elif log == "WARN_list":
#         "WARN_list" += 1
#     elif log == "ERROR_list":
#         "ERROR_list" += 1
#     else:
#         continue
    
# print(f"INFO_list: {}, WANR_list = {}, ERROR_list = {}")

# 2차 시도
# counts = {"INFO_list":0, "WARN_list":0, "ERROR_list":0}

# while True:
#     log = input("로그 레벨 입력: ").upper()
#     if log == "STOP":
#         break
#     elif log == "INFO":
#         counts["INFO_list"] += 1
#     elif log == "WARN":
#         counts["WARN_list"] += 1
#     elif log == "ERROR":
#         counts["ERROR_list"] += 1
#     else:
#         continue
    
# print(f"INFO_list: {counts["INFO"]}, WANR_list = {counts["WARN"]}, ERROR_list = {counts["ERROR"]}")

# 3차 시도
# counts = {"INFO":0, "WARN":0, "ERROR":0}

# while True:
#     log = input("로그 레벨 입력: ").upper()
#     if log == "STOP":
#         break
    
#     # 만약 입력받은 log가 딕셔너리의 "열쇠(Key)"들 중에 있다면?
#     for log in counts:
#         counts[" "] += 1
#     else:
#         print("잘못된 입력입니다.")
    
# print(f"INFO_list: {counts["INFO"]}, WANR_list = {counts["WARN"]}, ERROR_list = {counts["ERROR"]}")

# 4차 시도(정답)
counts = {"INFO":0, "WARN":0, "ERROR":0}

while True:
    log = input("로그 레벨 입력: ").upper()
    if log == "STOP":
        break
    
    # 만약 입력받은 log가 딕셔너리의 "열쇠(Key)"들 중에 있다면?
    if log in counts:
        counts[log] += 1
    else:
        print("잘못된 입력입니다.")
    
print(f"INFO: {counts['INFO']}, WANR = {counts['WARN']}, ERROR = {counts['ERROR']}")

# 5차 시도(응용)
# counts = {"INFO":0, "WARN":0, "ERROR":0}

# while True:
#     log = input("로그 레벨 입력: ").upper()
#     if log == "STOP":
#         break
    
#     # 만약 입력받은 log가 딕셔너리의 "열쇠(Key)"들 중에 있다면?
#     if log in counts:
#         counts.get[log, 0] += 1
#     else:
#         print("잘못된 입력입니다.")
    
# print(f"INFO: {counts[]}, WANR = {counts[]}, ERROR = {counts[]}")

# 6차 시도(응용)
# counts = {"INFO":0, "WARN":0, "ERROR":0}

# while True:
#     log = input("로그 레벨 입력: ").upper()
#     if log == "STOP":
#         break
    
#     # 만약 입력받은 log가 딕셔너리의 "열쇠(Key)"들 중에 있다면?
#     if log not in counts:
#         counts.get(log, 0)
#         counts[log] = 1

# for key, value in counts.items():
#     print(f"{key}: {value}", end = " ")

# 7차 시도(응용)
counts = {"INFO":0, "WARN":0, "ERROR":0}

while True:
    log = input("로그 레벨 입력: ").upper()
    if log == "STOP":
        break
    
    # 만약 입력받은 log가 딕셔너리의 "열쇠(Key)"들 중에 있다면?
    if log not in counts:        
        counts[log] = 1
    else:
        counts[log] += 1
    # counts[log] = counts.get(log, 0) + 1

for key, value in counts.items():
    print(f"{key}: {value}", end = " ")