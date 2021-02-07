# -*- coding:utf-8 -*-

import ast
import requests
from common.localconfig_utils import local_config

class RequestUtils():
    def __init__(self):
        self.hosts=local_config.URL
        self.headers={"ContenType":"application/json;charset=utf-8"}
        self.session=requests.session()

    def get(self,get_infos):
        url=self.hosts+get_infos["请求地址"]
        # print(url)
        response=self.session.get(url=url,
                                  params=ast.literal_eval(get_infos["请求参数(get)"])
                                  )
        print(response.text)
        response.encoding=response.apparent_encoding
        result={
            'code':0,   #请求是否成功的标志位
            'response_reason':response.reason,
            'response_code':response.status_code,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result


    def post(self, get_infos):
        url = self.hosts + get_infos["请求地址"]
        print(url)
        response = self.session.post(url=url,
                                    headers=self.headers,
                                    params={"access_token":"41_DqBOGbtePMJ35SbHwiESFFW1A8AISOYk-X_s-XC7c3ylXXa4oDQC15v3LufL8geBKlIMDooa_YIcPA36-caW1wqQAE3SF_KSHv_LREvWJf6o5lQDrAy6noSHFSujM1vog96Y-HA9HFFxU1LFDYPbAAAZUL"},
                                    # params=ast.literal_eval(get_infos["请求参数(get)"]),
                                    # data=get_infos["提交数据(post)"]
                                     json=ast.literal_eval(get_infos["提交数据(post)"])
                                    )

        response.encoding = response.apparent_encoding
        # print(response.json())
        print(response.text)
        result = {

            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result


if __name__=="__main__":
    get_infos={'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}
    # RequestUtils().get(get_infos)
    #字符串转为字典
    post_infos={'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":101}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    RequestUtils().post(post_infos)
    print(post_infos)
