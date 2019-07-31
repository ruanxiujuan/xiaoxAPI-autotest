import unittest
import logging
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from config.cif import case_dir, report_file, report_tile, report_description


def run_case():
    suite = unittest.defaultTestLoader.discover(case_dir)  # 自动加载所有用例

    logging.info("======================测试开始=====================")

    with open(report_file, 'wb') as f:
        HTMLTestRunner(stream=f,
                       title=report_tile,
                       description=report_description,
                       verbosity=2).run(suite)

    logging.info("======================测试结束=====================")


if __name__ == "__main__":
    run_case()