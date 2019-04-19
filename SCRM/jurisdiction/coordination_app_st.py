import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from SCRM.jurisdiction.currency import JurisdictionElement
from SCRM.common import LoginPublic

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class CoordinationApp(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15882223197', "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    def test_open_SkyDrive(self):
        """
        打开网盘管理权限，验证网盘管理是否存在

        1、使用超管账号，进入权限管理后台，切换至{协同应用}，打开{网盘管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/document/public};

        3、验证是否存在{上传}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='这是超管测试账号')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_open_SkyDrive()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[4])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_SkyDrive(self):
        """
        关闭网盘管理权限，验证网盘管理是否存在

        1、使用超管账号，进入权限管理后台，切换至{协同应用}，关闭{网盘管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/document/public};

        3、验证是否存在{新建文件}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='这是超管测试账号')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_close_SkyDrive()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[4])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
