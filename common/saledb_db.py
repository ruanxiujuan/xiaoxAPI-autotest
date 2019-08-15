import pymysql
from config.cif import SALEDB_DB


# 连接顾问端数据库
def get_saledb_db_connect():
    conn = pymysql.connect(**SALEDB_DB)
    return conn


# 查询数据库
def query_db(sql):
    conn = get_saledb_db_connect()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(sql, result)
    return result


# 修改数据库
def change_db(sql):
    conn = get_saledb_db_connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    print(sql)


# 查询订单
def query_order(sql):
    query_db(sql)


# 删除所有订单
def delete_order(sql):
    change_db(sql)


if __name__=="__main__":
    query_db("select * from orders where name like '小娟%'")
    # change_db()
    # query_order()
    # delete_order()
