
import os
from common.excel_utils import ExcelUtils
from common import config
from common.localconfig_utils import local_config

current_path=os.path.dirname(__file__)
test_data_path=os.path.join(current_path,'..',local_config.CASE_DATA_PATH)

class TestdataUtils():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path=test_data_path
        self.test_data=ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        testcase_dict={}
        for rwo_data in self.test_data:
            testcase_dict.setdefault(rwo_data['测试用例编号'],[]).append(rwo_data)
        return testcase_dict

    def def_testcase_data_list(self):
        testcase_list=[]
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict={}
            one_case_dict['case_name']=k
            one_case_dict['case_name']=v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__=="__main__":
    testdataUtils=TestdataUtils()
    for i in testdataUtils.def_testcase_data_list():
        print(i)

# {'case_name': [{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}]}
# {'case_name': [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag" : {"name" : "衡东8888"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":45158}', '测试结果': ''}]}
# {'case_name': [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}, {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag":{"id":408}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":1,"errmsg":"ok"}', '测试结果': ''}]}
