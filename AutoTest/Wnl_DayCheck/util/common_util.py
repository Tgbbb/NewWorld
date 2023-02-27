# coding:utf-8
# excel中的预期结果与实际结果对比
from AutoTest.Wnl_DayCheck.data import get_data


class CommonUtil():
    # def Str_Two(self):
    #
    def is_contain(self, goodsid_one, goodsid_two, purl_one, purl_two):
        # 判断一个字符串是否在另外一个字符串中
        # str_one:查找的字符串
        # str_two:被查找的字符串
        flag = None
        if goodsid_one == goodsid_two:
        # 1：产品链接错误，2：goodsid错误，3：没有问题
            if purl_one == purl_two:
                flag = 3
            else:
                flag = 1
        else:
            flag = 2

        return flag
