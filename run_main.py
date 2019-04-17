import unittest
import logging
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from config.cif import case_dir, report_file, report_tile, report_description
from case.test_get_rob_resources import TestGetRob
from case.test_rob_resource import TestRob


def run_case():
    suite = unittest.defaultTestLoader.discover(case_dir)  # 自动加载所有用例

    suite_rob = unittest.TestSuite()   # 加载抢单用例
    suite_rob.addTest(TestGetRob('test_get_rob_resources_list'))
    suite_rob.addTest(TestRob('test_rob_resource'))

    logging.info("======================测试开始=====================")

    with open(report_file, 'wb') as f:
        HTMLTestRunner(stream=f,
                       title=report_tile,
                       description=report_description,
                       verbosity=2).run(suite_rob)

    logging.info("======================测试结束=====================")


if __name__ == "__main__":
    run_case()