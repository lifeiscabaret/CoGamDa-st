--schema.sql

CREATE TABLE memo (
    memo_id INTEGER PRIMARY KEY AUTOINCREMENT, --고유번호
    title TEXT NOT NULL, --제목
    content TEXT --내용
);

--삽입 쿼리
INSERT INTO memo (title, content)
VALUES ('오늘 배운 내용', 'AI 서비스');

INSERT INTO memo (title, content)
VALUES ('기억할 거', 'SQlite, React 사용법')
