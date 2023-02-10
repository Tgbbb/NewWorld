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
        "cookie":"sadasdasdasdassdasasdas"
    }
    return header


