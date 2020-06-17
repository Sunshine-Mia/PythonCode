from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 浏览器复用登录企业微信
class TestLogin:
    def test_debug_login(self):
        option = Options()
        # 调试地址
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")