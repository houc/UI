from selenium.webdriver.common.by import By


class _OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver):
        self.driver = driver

    def F5(self):
        """浏览器刷新"""
        self.driver.refresh()



class ElementLocation(_OperationElement):
    """
    浏览器元素定位封装类
    """

    def __init__(self, driver):
        super(ElementLocation, self).__init__(driver)

    def XPATH(self, element: str, param=""):
        """
        结合selenium，封装一个xpath文字元素定位
        Usage:
            ElementLocation(self.driver).XPATH(手机号/邮箱*/../input!!send")
        """
        type_event = element.split('!!')[1]  # 执行的方式，如:send_keys/click....
        if '$' in element:
            first_path = element.split('$')[0]  # 如xpath中:div/a手机号/邮箱*/../input!!send#15928564313,截取前面路径:div/a
            text = element.split('$')[1].split('*')[0]  # element中参数进行截取处理，0即为文字
            path = element.split('*')[1].split('!!')[0]  # element中参数进行截取处理，1即为路径
            if type_event == "send":
                self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                         format(first_path, text, path)).send_keys(param)
            elif type_event == "click":
                self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                         format(first_path,text, path)).click()
            elif type_event == "text":
                value = self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                                 format(first_path, text, path)).text
                return value
            elif type_event == "display":
                value = self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                                 format(first_path, text, path)).is_displayed()
                return value
        else:
            text = element.split('*')[0]  # element中参数进行截取处理，0即为文字
            path = element.split('*')[1].split('!!')[0]  # element中参数进行截取处理，1即为路径
            first_path = '*'
            if type_event == "send":
                self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                         format(first_path, text, path)).send_keys(param)
            elif type_event == "click":
                self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                         format(first_path,text, path)).click()
            elif type_event == "text":
                value = self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                                 format(first_path, text, path)).text
                return value
            elif type_event == "display":
                value = self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                                 format(first_path, text, path)).is_displayed()
                return value

    def CSS(self, element: str, send=""):
        """
        结合selenium，封装一个CSS
        :param element: "input[name='wd']", "input[name]".....
        :param param: send_keys里面的参数
        :return: 对应元素值
        """
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).send_keys(send)
        elif type_event == "text":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).is_displayed()
            return value



if __name__ == '__main__':
    text = '手机号/邮箱*/../input!!send#15928564313'
    print(text.split('^'))