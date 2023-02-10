# coding:utf-8
from AutoTest.ImoocInterface.util.opexcel import OpExcel
from AutoTest.ImoocInterface.util.opjson import Opjson
from data_config import *
import json
from AutoTest.ImoocInterface.util import *


class Get_Data():  # file_path为文件路径，sheet_id为
    def __init__(self, file_path=None, sheet_id=None):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.file = OpExcel(self.file_path, self.sheet_id)

    def get_is_run(self, row):  # 判断该条用例是否执行
        flag = None
        col = get_run()
        run_model = self.file.op_data(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        col = get_Header()  # 判断是否有header
        header = self.file.op_data(row, col)
        if header == 'yes':
            return header_test_data()  # 如果有header就返回header的值，正常这个值存在json文件中去读取，这里写死举个例子
        else:
            return None

    # def get_ID(self, row):  # 获取数据的id
    #     col = get_id()
    #     ID = self.file.op_data(row, col)
    #     return ID
    def get_request_type(self, row):
        col = get_Request_Type()  # 判断是否有header
        request_type = self.file.op_data(row, col)
        return request_type

    def get_url(self, row):
        col = get_Url()
        url = self.file.op_data(row, col)
        return url

    def get_request_body(self, row):
        col = get_Request_Data()
        data_id = self.file.op_data(row, col)
        body = Opjson(self.file_path,data_id)
        request_data = body.get_jsondata()
        return request_data

    def get_datalines(self):  # 获取数据的行数
        lines = self.file.get_lines()
        return lines


if __name__ == '__main__':

    test = Get_Data('../configdata/useexm.xlsx', 0)
    print(test.get_request_body(1))

