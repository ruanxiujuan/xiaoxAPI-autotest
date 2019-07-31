import pymysql
from config.cif import SMART_COUNSELOR_DB



# 顾问端数据库
def smart_counselor_connect(db_conf=SMART_COUNSELOR_DB):
    conn = pymysql.connect(**db_conf)
    return conn


# 资源系统数据库
def resdb_connect():
    conn = pymysql.connect(
        host="192.168.0.137",
        port=3306,
        user="root",
        password="mirandA123!@#",
        db="test_resdb_db",
        charset="utf8"
    )
    return conn


# 销售系统数据库
def saledb_connect():
    conn = pymysql.connect(
        host="192.168.0.137",
        port=3306,
        user="root",
        password="mirandA123!@#",
        db="test_saledb",
        charset="utf8"
    )
    return conn