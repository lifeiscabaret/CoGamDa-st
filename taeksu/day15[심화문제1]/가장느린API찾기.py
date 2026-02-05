# 1. 변수 초기화 (1번 구간)
# 스크립트: "먼저, 가장 느린 응답 시간을 기록할 max_time을 -1로 초기화했습니다. 0이 아닌 -1로 
# 둔 이유는, 어떤 유효한 로그가 들어오더라도 즉시 첫 번째 기록으로 업데이트하기 위한 
# '기준점'을 잡기 위해서입니다. slowest_path는 가장 느린 API의 이름을 함께 기억할 이름표 역할을 합니다."
max_time = -1
slowest_path = ""

# 2. 메인 루프와 경로 검증 (2번 구간)
# 스크립트: "전체 로직은 while True 무한 루프로 동작하며 사용자의 입력을 기다립니다. 
# 첫 번째 입력인 API 경로에서 'STOP'이 들어오면 수집을 즉시 중단합니다. 만약 사용자가 실수로 
# 빈 값을 입력하면 EMPTY PATH라는 안내를 띄우고 continue를 통해 다시 경로 입력 단계로 
# 돌려보내 데이터의 무결성을 유지합니다."
while True:
    comparison_path = input("path:")  
    
    if comparison_path == "STOP":
        break
    
    elif comparison_path == "":
        print("EMPTY PATH")
        continue      

    # 3. 예외 처리의 핵심: 시간 입력 (3번 구간)
    # 스크립트: "가장 중요한 '응답 시간' 입력 구간입니다. 여기서는 중첩 while 루프와 파이썬의 
    # try-except 구문을 활용했습니다.
    # 첫째, int() 변환을 시도하여 숫자가 아닌 값이 들어오면 즉시 ValueError를 발생시키고 
    # INVALID TIME을 출력합니다. 아까 발견했던 -100 같은 음수 기호가 포함된 숫자도 안전하게 
    # 숫자로 먼저 인식하게 만듭니다.
    # 둘째, 숫자로 변환에 성공했더라도 0보다 작은 '음수'라면 NEGATIVE TIME을 출력하고 
    # 다시 입력을 요구합니다. 이 과정을 통해 오직 0 이상의 깨끗한 정수 데이터만 다음 
    # 단계로 넘어갈 수 있게 됩니다."
    while True:
        time_input = input("time:")      

        try:            
            time_val = int(time_input)
            
            if time_val < 0:
                print("NEGATIVE TIME")
                continue

            break
        
        except ValueError:            
            print("INVALID TIME")    

    
    # 4. 기록 갱신과 결과 출력 (4~5번 구간)
    # 스크립트: "검증이 끝난 데이터는 현재의 max_time과 비교합니다. 
    # 만약 방금 입력된 시간이 기존 기록보다 크다면, 시간값과 경로를 동시에 업데이트합니다. 
    # 마지막으로 'STOP' 명령으로 루프가 종료되면 결과를 발표합니다. 
    # 만약 유효한 로그가 하나도 없었다면 초기값인 -1을 확인해 NO LOGS를 띄우고, 
    # 데이터가 있다면 f-string을 사용해 가장 느린 API와 시간을 가독성 있게 출력하며 마무리합니다."
    current_time = int(time_input)
    
    if current_time > max_time:        
        max_time = current_time         
        slowest_path = comparison_path

if max_time == -1:
    print("NO LOGS")
else:    
    print(f"SLOWEST: {slowest_path} ({max_time}ms)")

# Q: 왜 isdigit() 대신 try-except를 썼나요?
# A: "기존의 .isdigit()은 마이너스 기호(-)나 플러스 기호(+)를 숫자로 인식하지 못해 
# INVALID TIME을 띄우는 한계가 있었습니다. 
# try-except는 파이썬이 처리할 수 있는 모든 숫자 형식을 가장 정확하고 안전하게 판별할 수 있는 
# 실무적인 방식이기 때문입니다."

# Q: 만약 똑같이 가장 느린 API가 2개라면 어떻게 되나요?
# A: "현재 로직은 current_time > max_time 즉, '초과'일 때만 갱신하므로, 
# 시간이 같다면 가장 먼저 입력된 API를 유지합니다. 
# 만약 가장 마지막에 입력된 것을 기록하고 싶다면 >=로 연산자를 바꾸면 됩니다."