

a={'one':1,'tow':2,'three':3}
# a['one']=3.2
a.setdefault('four',4)
a.setdefault('one',3.1)
print(a)

lista=[
    {'测试用例编号': 'api_case_01', '测试用例名称': '获取token接口测试', '用例执行': '是', '用例步骤': 'step_01'},
    {'测试用例编号': 'api_case_02', '测试用例名称': '机构列表接口测试', '用例执行': '是', '用例步骤': 'step_01'},
    {'测试用例编号': 'api_case_02', '测试用例名称': '机构列表接口测试', '用例执行': '是', '用例步骤': 'step_02'},
    {'测试用例编号': 'api_case_03', '测试用例名称': '机构列表接口测试', '用例执行': '否', '用例步骤': 'step_01'},
    {'测试用例编号': 'api_case_03', '测试用例名称': '机构列表接口测试', '用例执行': '否', '用例步骤': 'step_02'}
]

# case_list={}
# for i in lista:
#     case_list.setdefault('case_info',[]).append(i)
#
# print(case_list)

case_dict={}
for i in lista:
    case_dict.setdefault(i['测试用例编号'],[]).append(i)
# print(case_dict)

case_list=[]
for k,v in case_dict.items():
    case_dict={}
    case_dict['case_name']=k
    case_dict['case_info']=v
    case_list.append(case_dict)

for c in case_list:
    print(c)
#字典转列表





#
# all_case_list=[]
#
# for i in lista:
#     all_case={}
#     case_list.setdefault(i['测试用例编号'],[]).append(i)  #核心
#     all_case['case_name']=i['测试用例编号']
#     all_case['case_info']=case_list[i['测试用例编号']]
#     all_case_list.append(all_case)
# print(all_case_list)