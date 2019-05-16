#coding:utf-8
import unittest
import requests
sr=requests
import ddt
from ddt_data.getRegionList import getRegionList
rl=getRegionList(sr)
from public.log_out import logger
log=logger()

@ddt.ddt
class test_region(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    @ddt.data(*rl.list_data)
    def test_region_1(self,data):
        '''测试通过ID获取地区属性'''
        result=rl.get_region_true(data['canshu'])
#         self.assertEqual(data['code'], result['code'], msg=u'地区详情测试失败')
        self.assertIn( data['have'],result['regionList'][2]['name'], msg=u'地区详情测试失败')
        
if __name__=="__main__":
    unittest.main()
        
        