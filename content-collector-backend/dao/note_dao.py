from dao.util.dict_to_sql import dict_to_update_sql, dict_to_create_sql
from dao.util.connector import get_cursor


def create_note(note: dict):
    """
    添加一个记录
    :param note: 所有非空字段作为键组成的字典
    :return:影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        param = dict_to_create_sql(note)
        sql = f"INSERT INTO Note {param[0]} VALUES {param[1]}"
        values = param[2]
        cursor.execute(sql, values)
        return cursor.rowcount


def get_all_note():
    """
    :return: 所有记录
    """
    with get_cursor() as cursor:
        sql = "SELECT * FROM Note ORDER BY id DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        return data


def get_note_by_id(note_id):
    """
    :param note_id:
    :return: 特定id的记录
    """
    with get_cursor() as cursor:
        sql = f"SELECT * FROM Note WHERE id = ?"
        cursor.execute(sql, (note_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_note(note_id, updates):
    """
    更新指定id的记录
    :param note_id:
    :param updates: 待更新字段作为键组成的字典
    :return: 影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        param = dict_to_update_sql(updates)
        sql = f"UPDATE Note SET {param[0]} WHERE id = ?"
        values = param[1] + (note_id,)
        cursor.execute(sql, values)
        return cursor.rowcount


def delete_note(note_id):
    """
    删除指定id的记录
    :param note_id:
    :return: 影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        sql = "DELETE FROM Note WHERE id = ?"
        cursor.execute(sql, (note_id,))
        return cursor.rowcount


def reset_table(table_name="Note"):
    """
    清空表，重置主键自增
    :param table_name:
    :return:
    """
    with get_cursor() as cursor:
        cursor.execute(f"DELETE FROM {table_name}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")
