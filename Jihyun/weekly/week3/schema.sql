-- schema.sql
DROP TABLE IF EXISTS memo;

CREATE TABLE memo (
    memo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT
);

-- (선택) 샘플 데이터 넣기
INSERT INTO memo (title, content) VALUES
('메모1', '내용1'),
('메모2', '내용2'),
('메모3', '내용3');
