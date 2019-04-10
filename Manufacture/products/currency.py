import requests
import time

from model.Yaml import MyProject
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def read_currency(keys: str, line: int):
    """
    读取currency.ya中的数据
    Usage: 
        url = MyYaml("SCRM").base_url + read_currency("get_customer", 0)
        data = read_currency("get_customer", 1)
    """
    data = []
    read = MyProject(UP_FILE_NAME, keys).module_data
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]

def token():
    """
    获取token值
    Usage:
        r = requests.post(url, headers=token(), data=data, stream=True)
    """
    return ConfigParameter().read_ini()


class ProductsElement(OperationElement):
    """
    封装"ProductsElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    switch_table = (By.XPATH, "//div[contains(@class, 'p_ProductList')]/div/div[$]")
    img = (By.XPATH, "(//div[@class='projectitem'])[$]")

    def table_click(self, location):
        """
        product里面的center切换点击
        :param location: 1:Automotive filter series, 2:Automotive Brake, 3:Compressor, 4:Seal series/ oil seal
                         5:Motor drain valve, 6:Shock absorber, 7:Rubber Miscellaneous items,
                         8:General rubber parts
        :return: ...
        """
        self.is_click(self.str_conversion(self.switch_table, location))

    def img_click(self, location):
        """
        对应模块进入详情，点击图片进入详情
        :param location: 第几张图片进入详情
        :return: ...
        """
        self.is_click(self.str_conversion(self.img, location))