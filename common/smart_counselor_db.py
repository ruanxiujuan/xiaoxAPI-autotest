import pymysql
from config.cif import SMART_COUNSELOR_DB
import logging


# 连接顾问端数据库
def get_smart_counselor_db_connect(db_conf=SMART_COUNSELOR_DB):
    conn = pymysql.connect(**db_conf)
    return conn


# 查询数据库
def query_db(sql):
    conn = get_smart_counselor_db_connect()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    logging.info("执行查询sql:{}".format(sql))
    logging.info("查询结果为：{}".format(result))
    return result


# 修改数据库
def change_db(sql):
    conn = get_smart_counselor_db_connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    logging.info("执行修改sql:{}".format(sql))

