from dao.util.dict_to_sql import dict_to_update_sql, dict_to_create_sql
from dao.util.connector import get_cursor


def create_tablename_snackcase(tablename_snackcase: dict):
    """
    添加一个记录
    :param tablename_snackcase: 所有非空字段作为键组成的字典
    :return:影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        param = dict_to_create_sql(tablename_snackcase)
        sql = f"INSERT INTO TableNameOrigin {param[0]} VALUES {param[1]}"
        values = param[2]
        cursor.execute(sql, values)
        return cursor.rowcount


def get_all_tablename_snackcase():
    """
    :return: 所有记录
    """
    with get_cursor() as cursor:
        sql = "SELECT * FROM TableNameOrigin"
        cursor.execute(sql)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        return data


def get_tablename_snackcase_by_id(tablename_snackcase_id):
    """
    :param tablename_snackcase_id:
    :return: 特定id的记录
    """
    with get_cursor() as cursor:
        sql = f"SELECT * FROM TableNameOrigin WHERE id = ?"
        cursor.execute(sql, (tablename_snackcase_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_tablename_snackcase(tablename_snackcase_id, updates):
    """
    更新指定id的记录
    :param tablename_snackcase_id:
    :param updates: 待更新字段作为键组成的字典
    :return: 影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        param = dict_to_update_sql(updates)
        sql = f"UPDATE TableNameOrigin SET {param[0]} WHERE id = ?"
        values = param[1] + (tablename_snackcase_id,)
        cursor.execute(sql, values)
        return cursor.rowcount


def delete_tablename_snackcase(tablename_snackcase_id):
    """
    删除指定id的记录
    :param tablename_snackcase_id:
    :return: 影响行数，1说明执行成功，0说明执行失败
    """
    with get_cursor() as cursor:
        sql = "DELETE FROM TableNameOrigin WHERE id = ?"
        cursor.execute(sql, (tablename_snackcase_id,))
        return cursor.rowcount


def reset_table(table_name="TableNameOrigin"):
    """
    清空表，重置主键自增
    :param table_name:
    :return:
    """
    with get_cursor() as cursor:
        cursor.execute(f"DELETE FROM {table_name}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")
