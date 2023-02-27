# coding:utf-8
# 封装操作jason的包

import json

import chardet


# fp = open('../configdata/Data.json')
# data = json.load(fp)
# print(data['commonbody'])


class Opjson():
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = '../configdata/Data.json'

    # 读取json文件
    def request_data(self):
        # fp = open(self.filepath)
        # with open(self.filepath,encoding='gb18030',errors='ignore') as fp:
        with open(self.filepath) as fp:
            data = json.load(fp)
        return data

    # 并根据关键词获取数据
    def get_jsondata(self, data_id):
        if data_id == None:
            pass
        else:
            return self.request_data()[data_id]


if __name__ == '__main__':
    opjson = Opjson('../configdata/Data.json')
    request_data = opjson.get_jsondata("commonbody")
    print(request_data)
    # a = "commonbody".encode('utf-8')
    # b = chardet.detect(a)
    # print(b)
