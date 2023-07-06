DROP TABLE IF EXISTS Note;
-- 创建笔记表
CREATE TABLE Note (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- 笔记ID，主键，自增长
  title TEXT, -- 标题
  content TEXT NOT NULL, -- 内容，非空
  modify_time DATETIME NOT NULL -- 修改时间，非空
);