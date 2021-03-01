
import re
import ast

#正则匹配测试
#实际结果
str1='{"access_token":"42_YyirAyHpmx-JVx-_iN2g657v8dz6pixvlfAOADLW6BEqP1g6CRyjGTXLmkaISkwQpDx4CKklxDf_GazZWZlTEk04yuEkIKq5G3NHkmxCrwnbJ9oUT_j7Nqoh6FkqwSJnGfZ4JjpdlxqKo6AmYJHgADALWU","expires_in": 7200}'

#期望结果
str2='{"access_token":"(.+?)","expires_in":(.+?)}'

# print(re.findall(str2,str1))

# print(str1,str2)
if re.findall(str2,str1):
    print(True)
else:
    print(False)


#是否包含json key
jsondata1=ast.literal_eval(str1)
str2='access_token,expires_in'
check_key_list=str2.split(',')
for check_key in check_key_list:
    result=True
    if check_key in jsondata1.keys():
        result = True
    else:
        result = False
    if not result:
        break
print(result)
# print('access_token' in jsondata1.keys())


#键值对正确的情况
str2='{"expires_in":7200}'
for v in ast.literal_eval(str2).items():
    result=True
    if v in jsondata1.items():
        result = True
    else:
        result = False
    if not result:
        break
print(result)
# print(str2 in jsondata1.items())
