import sqlite3
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

def get_db_connection():
    # 힌트: row_factory 설정을 찾아보세요.
    # 이걸 설정 안 하면 데이터가 (1, '제목', '내용')처럼 튜플로 나와서
    # 나중에 JSON으로 만들 때 곤란해집니다.
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row # 이 줄이 아주 중요한 힌트입니다!
    return conn

@app.get("/memos")
async def read_memo():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM memos ORDER BY memo_id DESC").fetchall()
    return [dict(row) for row in rows]

@app.post("/memos")
async def create_memo(title: str, content: str = ""):
    # title: 필수 (str)
    # content: 선택 (기본값 "")
    conn = get_db_connection()
    cursor = conn.cursor() # 볼펜을 꺼냅니다.
    
    if not title.strip():
        raise HTTPException(status_code=400, detail="TITLEREQUIRED") 
    
    # SQL 명령 실행
    cursor.execute(
        "INSERT INTO memos (title, content) VALUES (?, ?)", (title, content)
    )

    # ⚠️ 중요! 저장을 확정 짓는 도장을 찍어야 합니다.
    conn.commit()

    # 방금 생성된 ID 가져오기
    new_id = cursor.lastrowid

    return {"memo_id": new_id, "title": title, "content": content}


# 1. 연결 통로 열기
conn = sqlite3.connect("app.db")
# 2. 볼펜(cursor) 꺼내기
cur = conn.cursor()
# 3. 볼펜으로 장부(DB)에 명령 적기(여기서 CREATE TABLE 실행!)
cur.execute("""
CREATE TABLE IF NOT EXISTS memos (
    memo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
""") 

conn.commit()

conn.close()