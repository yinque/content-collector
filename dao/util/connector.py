import os
import sqlite3
from contextlib import contextmanager

# 获取当前模块的文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建数据库文件的相对路径
DB_PATH = os.path.join(current_dir, "../../database.db")


@contextmanager
def get_cursor(title=True):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if title:
        # 设置游标的 row_factory 属性为 sqlite3.Row，结果带标题
        cursor.row_factory = sqlite3.Row

    try:
        yield cursor
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
