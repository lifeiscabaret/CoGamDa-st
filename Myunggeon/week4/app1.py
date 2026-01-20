'''
문제
다음과 같은 로그 레벨이 있다.
"INFO"
"WARN"
"ERROR"
사용자로부터 로그 레벨을 여러 번 입력받아,
각 레벨이 몇 번 나왔는지 출력하시오.
"STOP" 입력 시 종료
대소문자 구분 없음
'''

# 로그 레벨? 로그 메세지의 중요도를 단계로 나눈 기준

# 변수 설정
# info_val = 0
# warn_val = 0
# error_val = 0
#이렇게 쓰면 안됨. 이 값을 바로 딕셔너리에 저장하기 때문에 int는 불변 객체라서 값이 바뀌면 새 객체로 교체된다.
# info_val +=1 이렇게 하면 기존 0이 1로 수정되는 것이 아니라 1이라는 새로운 객체로 다시 바인딩

log_dic ={
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0
}
while True:
    log_lv = input("로그 레벨을 입력하세요: ").strip().upper() # 공백제거, 대문자화
    if log_lv == "INFO":
        log_dic["INFO"] += 1
    elif log_lv == "WARN":
        log_dic["WARN"] += 1
    elif log_lv == "ERROR":
        log_dic["ERROR"] += 1    
    elif log_lv == "STOP":
        break

print(log_dic)

'''
더 간단한 코드

log_dic = {
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0
}

while True:
    log_lv = input("로그 레벨을 입력하세요: ").strip().upper()

    if log_lv == "STOP":
        break
    elif log_lv in log_dic:
        log_dic[log_lv] += 1

print(log_dic)

'''