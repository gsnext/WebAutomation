from selenium import webdriver

self.driver=webdriver.Chrome("/Users/gsnext/Downloads/chromedriver")

class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    link_logout_linktext="Logout"
    driver = webdriver.Chrome("/Users/gsnext/Downloads/chromedriver")

    def __init__(self, driver):
        self.driver=webdriver.Chrome("/Users/gsnext/Downloads/chromedriver")

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id)


