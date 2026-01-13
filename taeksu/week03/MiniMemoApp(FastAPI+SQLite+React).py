import sqlite3
from fastapi import FastAPI

app = FastAPI()

def get_db_connection():
    # 힌트: row_factory 설정을 찾아보세요.
    # 이걸 설정 안 하면 데이터가 (1, '제목', '내용')처럼 튜플로 나와서
    # 나중에 JSON으로 만들 때 곤란해집니다.
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row # 이 줄이 아주 중요한 힌트입니다!
    return conn

@app.get("/memos")
async def read_memos ():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM memos_id ORDER BY DESC").fetchall()
    [dict(row) for row in rows]
    return

@app.post("/memos")

# 1. 연결 통로 열기
conn = sqlite3.connect("app.db")
# 2. 볼펜(cursor) 꺼내기
cur = conn.cursor()
# 3. 볼펜으로 장부(DB)에 명령 적기(여기서 CREATE TABLE 실행!)
cur.execute("""
CREATE TABLE memos (
    memo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
)
""") 

conn.commit()

conn.close()