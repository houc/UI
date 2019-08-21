import re

from model.MyDB import MyDB
from model.Yaml import MyConfig
from model.TimeConversion import standard_time


class MyAsserts:
    def __init__(self, first, second, id, level, name, case_scene, status, reason, url, time,
                 driver, module, screenshots_path, author, myself, error_path, log=None,
                 encoding='utf8', *, case_remark):
        self.first = first
        self.second = second
        self.id = id
        self.level = level
        self.name = name
        self.case_scene = case_scene
        self.status = status
        self.reason = reason
        self.url = url
        self.time = time
        self.driver = driver
        self.screenshots_path = screenshots_path
        self.author = author
        self.myself = myself
        self.log = log
        self.error_path = error_path
        self.module = module
        self.encoding = encoding
        self.case_remark = case_remark
        self.img_path = None
        self.thread = MyConfig('thread').config
        self.project = MyConfig('project_name').excel_parameter

    def asserts(self):
        """用例断言"""
        if self.reason is not None:
            if 'AssertionError' in str(self.reason):
                self.status = '失败'
            else:
                self.status = '错误'
            self.reason = self._strConversion(self.reason)
            self.img_path = self.screenshots_path
            self._log(self.reason)
        else:
            self.status = '成功'
            self.reason = self._strConversion(self.first)
        self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库,判断采用的数据库类型"""
        insert_time = standard_time()
        MyDB().insert_data(self.id, self.level, self.module, self.name,
                           self._strConversion(self.case_scene),
                           f'{self.time:.2f}秒', status, self.url, insert_time,
                           img_path, reason, self._strConversion(self.author),
                           results_value=self._strConversion(self.second),
                           case_remark=self._strConversion(self.case_remark))

    @staticmethod
    def _strConversion(values: str):
        """字符串中包含单引号转义成``"""
        return re.sub("'", "`", str(values)).replace('\\', '/').replace('"', "`").replace('%', '//')

    def _log(self, reason):
        """记录日志"""
        self.log.info(f'错误路径:{self.error_path},错误原因:{reason}')

