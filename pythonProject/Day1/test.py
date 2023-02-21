import json
def request_data(self):
    # fp = open(self.filepath)
    # with open(self.filepath,encoding='gb18030',errors='ignore') as fp:
    with open(self.filepath) as fp:
        data = json.load(fp)
    return data


# 并根据关键词获取数据
def get_jsondata(self, data_id):
    return self.request_data()[data_id]

