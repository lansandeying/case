#coding:utf-8
import unittest
import requests
import ddt
sr=requests
from ddt_data.sys_login_action import get_login
lg=get_login(sr)
from public.log_out import logger
log=logger()

@ddt.ddt
class test_login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_login_1(self):
        '''测试登录成功'''
        result=lg.post_login_s()
        self.assertEqual(u'成功', result['msg'], msg=u'登录成功测试失败')
        self.assertEqual(u'0000', result['code'], msg=u'登录成功测试失败')
#         {'msg': '成功', 'code': '0000', 'expire': 43200, 'token': 'a6ec9acdeacf6d8e006901ff3d36babd'}
    @ddt.data(*lg.list_data)
    def test_login_2(self,data):
        '''测试登录失败'''
        result=lg.post_login_f(data)
        self.assertEqual(data['msg'], result['msg'], msg=u'登录失败测试失败')
        self.assertEqual(data['code'], result['code'], msg=u'登录失败测试失败')
        
if __name__=="__main__":
    unittest.main()
        
        
