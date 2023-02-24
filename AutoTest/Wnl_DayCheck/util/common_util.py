# coding:utf-8
# excel中的预期结果与实际结果对比
from AutoTest.Wnl_DayCheck.data import get_data


class CommonUtil():
    # def Str_Two(self):
    #
    def is_contain(self, goodid_one, goodsid_two, purl_one, purl_two):
        # 判断一个字符串是否在另外一个字符串中
        # str_one:查找的字符串
        # str_two:被查找的字符串
        flag = None
        if goodid_one in goodsid_two:

            if purl_one in purl_two:
                pass
            else:
                print('产品链接错误，请检查')
            flag = True
        else:
            flag = False
        return flag
