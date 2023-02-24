# coding:utf-8
# excel中的预期结果与实际结果对比
from AutoTest.ImoocInterface.data import get_data


class CommonUtil():
    # def Str_Two(self):
    #
    def is_contain(self, str_one, str_two):
        # 判断一个字符串是否在另外一个字符串中
        # str_one:查找的字符串
        # str_two:被查找的字符串
        flag = None
        if str_one in str_two:
            # 做字符串比较时
        # if str_one == str_two:
            # int类型比较时
            flag = True
        else:
            flag = False
        return flag
