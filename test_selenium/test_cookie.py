import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# cookie登录企业微信
class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until((expected_conditions.element_to_be_clickable
                                                        ((By.ID, "menu_index"))))
            if res:
                break
        # 这里需要首次扫码登录
        # 获得cookie，是一个字典列表
        cookies = self.driver.get_cookies()
        # 将获取到的cookie 存放到json文件中，不需要格式转换
        with open("cookie.json", 'w') as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 由于selenium的cookies不支持expiry，所以需要去掉
            if "expiry" in cookie.keys():
                # dict支持pop的删除函数
                cookie.pop("expiry")
            # 添加一个dict的cookie信息
            self.driver.add_cookie(cookie)
        # 如果代码没有问题，但还是没有成功，多加等待时间
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 5).until((expected_conditions.element_to_be_clickable
                                                       ((By.ID, "menu_index"))))
            if res:
                break
        # excpted_conditions.xxx   都需要传入的是一个元组
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable
                                            ((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located
                                            ((By.ID, "js_upload_file_input")))
        # send_deys("绝对路径")
        self.driver.find_element_by_id("js_upload_file_input"). \
            send_keys("E:/Workspaces/PycharmProjects/PythonCode/test_selenium/data.xlsx")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located
                                            ((By.ID, "upload_file_name")))
        assert "data.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        self.driver.find_element_by_id("submit_csv").click()


