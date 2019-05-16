#coding:utf-8
import unittest
import os

case_path=os.path.join(os.getcwd(),"case")
report_path=os.path.join(os.getcwd(),"report")

discover=unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
print(discover)