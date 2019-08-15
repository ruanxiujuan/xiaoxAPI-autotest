''' 配置文件 '''
import os
import time
import logging

# 项目路径配置
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
case_dir = os.path.join(base_dir, 'case')  # 用例目录
data_dir = os.path.join(base_dir, 'data_file')  # 数据目录
log_dir = os.path.join(base_dir, 'logs')   # 日志目录
report_dir = os.path.join(base_dir, 'report')  # 测试报告路径


# 数据配置
data_file = os.path.join(data_dir, '0.png')


# 测试报告配置
report_file = os.path.join(report_dir, 'report.html')
report_tile = "顾问端自动化测试报告"
report_description = "顾问端接口自动化测试报告"


# 日志配置
today = time.strftime("%Y%m%d", time.localtime(time.time()))
console_handler = logging.StreamHandler()
# log_file = os.path.join(log_dir, "{}.log".format(today))
log_file = os.path.join(log_dir, "log.txt")
file_handler = logging.FileHandler(log_file, encoding="utf-8")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s %(lineno)d %(funcName)s %(levelname)s %(message)s",
                    handlers=[console_handler, file_handler])

# 数据库配置
# 1. 顾问数据库
SMART_COUNSELOR_DB = {
    "host": "192.168.0.137",
    "port": 3306,
    "user": "root",
    "password": "mirandA123!@#",
    "db": "test_smart_counselor",
    "autocommit": True
}
# 2. 资源系统数据库
RESDB_DB = {
    "host": "192.168.0.137",
    "port": 3306,
    "user": "root",
    "password": "mirandA123!@#",
    "db": "test_resdb_db",
    "autocommit": True
}
# 3. 销售系统数据库
SALEDB_DB = {
    "host": "192.168.0.137",
    "port": 3306,
    "user": "root",
    "password": "mirandA123!@#",
    "db": "test_saledb",
    "autocommit": True
}