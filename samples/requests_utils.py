# -*- coding:utf-8 -*-

import ast
import requests
import jsonpath
from common.localconfig_utils import local_config

class RequestUtils():
    def __init__(self):
        self.hosts=local_config.URL
        self.headers={"ContentType":"application/json;charset=utf-8"}
        self.session=requests.session()
        self.temp_variables={}  #存放临时变量

    def __get(self,get_info):
        url=self.hosts+get_info["请求地址"]
        # print(url)
        response=self.session.get(url=url,
                                  params=ast.literal_eval(get_info["请求参数(get)"])
                                  )
        # print(response.text)
        response.encoding=response.apparent_encoding

        if get_info["取值方式"]=="json取值":
            value=jsonpath.jsonpath(response.json(),get_info["取值代码"])[0]
            self.temp_variables[get_info["传值变量"]]=value
            # print(self.temp_variables)

        result={
            'code':0,   #请求是否成功的标志位
            'response_reason':response.reason,
            'response_code':response.status_code,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result


    def __post(self, post_info):
        url = self.hosts + post_info["请求地址"]
        print(url)
        response = self.session.post(url=url,
                                    headers=self.headers,
                                    params=ast.literal_eval(post_info["请求参数(get)"]),
                                    # data=get_info["提交数据(post)"]
                                     json=ast.literal_eval(post_info["提交数据(post)"])
                                    )

        response.encoding = response.apparent_encoding

        if post_info["取值方式"]=="json取值":
            value=jsonpath.jsonpath(response.json(),post_info["取值代码"])[0]
            self.temp_variables[post_info["传值变量"]]=value
            # print(self.temp_variables)

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

    def request(self,step_infos):
        request_type=step_infos["请求方式"]
        if request_type=="get":
            result=self.__get(step_infos)
        elif request_type=="post":
            result=self.__post(step_infos)
        else:
            result={'code':3,'result':'请求方式不支持'}
        # print(result['response_body'])
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            temp_result=self.request(step_info)
            if temp_result['code']!=0:
                break
        return temp_result


if __name__=="__main__":
    get_infos={'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}

    # get_info={'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}
    RequestUtils().request(get_infos)
    #字符串转为字典
    # post_infos={'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)':'{"tag":{"id":102}}', '取值方式': '无', '传值变量':'', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    # RequestUtils().post(post_infos)
    # case_info = [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx15938bc8b042cee0","secret":"f01c3e1836d6b40fb24db5dbc0142253"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag" : {"name" : "nanyue_8888"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"8888"}}'}]
    # requestUtils=RequestUtils()
    # for c in case_info:
    #     requestUtils.request(c)


