# coding:utf-8
import unittest
from public.public_file import browser
from page.page_login import LoginPage, login_url
class Login_test(unittest.TestCase):
    u'''登录页面的 case'''
    def setUp(self):
        self.driver = browser("chrome")
        self.login= LoginPage(self.driver) #login 参数是LoginPage 的实例
        self.login.open(url=login_url,text=u"用户登录 - 博客园")
    def login_case(self, username, psw, expect=True):
        '''登录用例的方法,'''
        # 第 1 步：输入账号
        self.login.input_username(username)
        # 第 2 步: 输入密码
        self.login.input_password(psw)
        # 第 3 步：点登录按钮
        self.login.click_submit()
        # 第 4 步：测试结果,刞断是否登录成功
        result =self.login.get_text_present(locator=("id","lnk_current_user"), text=u"懒散的鹰")
        # 第 5 步：期望结果
        expect_result = expect
        self.assertEqual(result, expect_result)
    def test_login01(self):
        u'''输入正确账号密码'''
        self.login_case("abc516015922", "711454466.cn", True)
    def test_login02(self):
        u'''输入错诨账号密码'''
        self.login_case("xx", "xx", False)
    def tearDown(self):
#         self.driver.quit()
        pass
if __name__ == "__main__":
    unittest.main()