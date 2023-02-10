# coding:utf-8
# 封装操作jason的包

import json


# fp = open('../configdata/Data.json')
# data = json.load(fp)
# print(data['commonbody'])


class Opjson():
    def __init__(self, filepath=None, data_id=None):
        self.filepath = filepath
        self.data_id = data_id

    # 读取json文件
    def request_data(self):
        # fp = open(self.filepath)
        # with open(self.filepath,encoding='gb18030',errors='ignore') as fp:
        with open(self.filepath) as fp:
            data = json.load(fp)
        return data

    # 并根据关键词获取数据
    def get_jsondata(self):
        return self.request_data()[self.data_id]


if __name__ == '__main__':
    opjson = Opjson('../configdata/Data.json', "commonbody")
    request_data = opjson.get_jsondata()
    print(request_data)
