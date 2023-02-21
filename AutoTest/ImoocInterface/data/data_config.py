# coding:utf-8
class global_var():
    # case_id
    Id = 0
    run = 1
    Url = 2
    Request_Type = 3
    Header = 4
    case_depend = 5
    data_depend = 6
    field_depend = 7
    Request_Data = 8
    Expect = 9
    Result = 10


def get_id():
    return global_var().Id


def get_run():
    return global_var().run


def get_Url():
    return global_var().Url


def get_Request_Type():
    return global_var().Request_Type


def get_Header():
    return global_var().Header


def get_case_depend():
    return global_var().case_depend


def get_data_depend():
    return global_var().data_depend


def get_field_depend():
    return global_var().field_depend


def get_Request_Data():
    return global_var().Request_Data


def get_Expect():
    return global_var().Expect


def get_Result():
    return global_var().Result


def header_test_data():
    header = {
        'method': 'POST',
        'authority': 'c.51wnl-cq.com',
        'scheme': 'https',
        'path': '/contentapi/api4.4.0/UserFback/UploadMsg',
        'content-length': '128',
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://mobile.51wnl-cq.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.159 Mobile Safari/537.36 ylna/1.0(mixad;kwtp;jrttsp;jrtttpsnf;gdtpl;jrttmr;ylad;jrttmsn;jrttmsp;mixpad;kwsn;ylspad;jrtt;kwsp;jrtttpsn;kw;xg;xmad;baidusp;jrtttp;xm;jdsp;xmsn;gdtsn;baidu;gdtv2;xmsp;gdtsp;jrttm;baidusn;jdad;)  wnlver/6002006 wnl 6.2.6',
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://mobile.51wnl-cq.com/feedback/?pushToken=AsxMhEO8ouBZlH-15f-hiHTvMmSEL_sebeqWQBpm-IVr&osver=8.1.0&appver=6.2.6&deviceType=16th&deviceId=ceba49ff223e6af516c629f3a02b7a2d&userId=qq20210611102810514&versioncode=6002006',
        'accept-encoding': 'gzip, deflate',
        'accept-language	': 'zh-CN,en-US;q=0.9',
        'x-requested-with': 'com.youloft.calendar'
    }
    return header
