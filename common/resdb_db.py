import pymysql
from config.cif import RESDB_DB


# 连接顾问端数据库
def get_resdb_db_connect():
    conn = pymysql.connect(**RESDB_DB)
    return conn


# 查询数据库
def query_db(sql):
    conn = get_resdb_db_connect()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(sql, result)
    return result


# 修改数据库
def change_db(sql):
    conn = get_resdb_db_connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    print(sql)


