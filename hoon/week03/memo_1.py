from fastapi import FastAPI, HTTPException, Query
import sqlite3
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
import os
# 수명 주기 관리를 위한 도구 임포트
from contextlib import asynccontextmanager

# 1. 데이터베이스 파일 이름 설정
DATABASE = 'app.db'

# 2. 데이터베이스 연결 헬퍼 함수
# 반복되는 DB 연결 코드를 줄이기 위해 별도 함수로 분리
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    # 조회된 데이터를 딕셔너리처럼 컬럼명으로 다룰 수 있게 설정 (row['id'] 등)
    conn.row_factory = sqlite3.Row
    return conn

# 3. Lifespan(수명 주기) 매니저 정의
# @asynccontextmanager 데코레이터는 함수를 '컨텍스트 매니저'로 만든다
# 이 함수는 앱이 시작될 때와 종료될 때의 로직을 한 곳에서 관리
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- [Startup 구역] 앱이 실행되기 직전 ---
    # DB 파일 존재하는지 확인하고, 없다면 테이블 생성
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE memo (
                memo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT
            );
        ''')
        conn.commit()  # 변경 사항 저장
        conn.close()   # 연결 종료
        print("초기화 완료: DB와 테이블이 생성되었습니다.") #표시해주면 좋음
    
    # --- [Yield] 앱 실행 중 ---
    # yield 키워드는 여기서 함수의 실행을 '일시 정지' 시키고 제어권을 FastAPI에게 넘긴다
    # 즉, 이 시점부터 서버가 켜지고 API 요청(GET, POST 등)을 받기 시작
    yield
    
    # --- [Shutdown 구역] 앱이 종료될 때 ---
    # 사용자가 Ctrl+C를 눌러 서버를 끌 때 실행
    # 열려있는 리소스나 연결이 있다면 여기서 닫음
    print("서버 종료: 리소스를 정리합니다.") #표시해주면 좋음

# 4. FastAPI 앱 인스턴스 생성
# 위에서 정의한 lifespan 함수를 파라미터로 전달하여 연결
app = FastAPI(lifespan=lifespan)

# 5. CORS 미들웨어 설정
# 보안상 막혀있는 브라우저(React)의 접근 권한을 열어준다
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드(GET, POST, DELETE...) 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# --- API 엔드포인트 ---

# 6. 메모 목록 조회 (GET)
@app.get("/memos", response_model=List[Dict])
def get_memos():
    # DB 연결 열기
    conn = get_db_connection()
    # 최신순 정렬 조회
    memos = conn.execute('SELECT memo_id, title, content FROM memo ORDER BY memo_id DESC').fetchall()
    # DB 연결 닫기
    conn.close()
    # 결과를 딕셔너리 리스트로 변환하여 반환
    return [dict(memo) for memo in memos]

# 7. 메모 추가 (POST)
@app.post("/memos", response_model=Dict)
def add_memo(title: str = Query(...), content: str = Query("")):
    # 앞뒤 공백 제거
    title = title.strip()
    content = content.strip()

    # 제목 유효성 검사: 비어있으면 400 에러 발생
    if not title:
        raise HTTPException(status_code=400, detail="TITLE REQUIRED")

    # DB 연결 및 데이터 삽입
    conn = get_db_connection()
    cursor = conn.cursor()
    # 보안: SQL Injection 방지를 위해 '?' 사용
    cursor.execute('INSERT INTO memo (title, content) VALUES (?, ?)', (title, content))
    conn.commit() # 저장 확정
    
    # 방금 생성된 ID 가져오기
    memo_id = cursor.lastrowid
    conn.close()

    # 프론트엔드 갱신을 위해 저장된 데이터 반환
    return {"memo_id": memo_id, "title": title, "content": content}