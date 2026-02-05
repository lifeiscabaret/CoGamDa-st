'''
jaeyeon.day13.problem_2의 Docstring

[응용 문제 1] 간단 로그 카운터
문제
다음과 같은 로그 레벨이 있다.
•	"INFO"
•	"WARN"
•	"ERROR"
사용자로부터 로그 레벨을 여러 번 입력받아,
각 레벨이 몇 번 나왔는지 출력하시오.
•	"STOP" 입력 시 종료
•	대소문자 구분 없음
👉 출력 예
INFO: 3 WARN: 1 ERROR: 2 
👉 포인트
•	딕셔너리 카운트
•	문자열 전처리
•	루프 종료 조건

'''

dict_logLable_cnt = {
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0,
}

while True:
    input_user_logLable = input("입력: ")
    input_user_logLable_lower = input_user_logLable.lower()
    if input_user_logLable_lower == "stop":
        print("종료")
        break
    elif input_user_logLable_lower == "info":
        dict_logLable_cnt["INFO"]+=1
    elif input_user_logLable_lower == "warn":
        dict_logLable_cnt["WARN"]+=1
    elif input_user_logLable_lower == "error":
        dict_logLable_cnt["ERROR"]+=1

result = f"INFO: {dict_logLable_cnt['INFO']} WARN: {dict_logLable_cnt['WARN']} ERROR: {dict_logLable_cnt['ERROR']}"
print(result)