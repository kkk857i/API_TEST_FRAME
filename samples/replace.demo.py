
import re
import ast
import requests

temp_varables={"token":"hello"}

params='{"access_token":${token}}'   #建议考虑1个以上的情况
value=re.findall('\\${\w+}',params)[0]
print(value)
params=params.replace(value,'"%s"'%temp_varables.get(value[2:-1]))
print(params)

temp_varables={"token":"123456","number":"123","age":"66"}
str1='{"access_token":${token},${age}==>${number}}'
# for v in re.findall('\\${\w+}',str1):
#     str1=str1.replace(v,temp_varables.get(v[2:-1]))
# print(str1)

# str1=re.sub('\\${\w+}',str1)


temp_varables={}

#第一个用例，添加标签
temp_varables["token"]="35_an_"

# temp_varables={}

#第二个用例删除标签
temp_varables["token"]="35555"

print(temp_varables)






# requests.get(url="/cgi-bin/ta
# gs/delete",
#              params=ast.literal_eval(params)
#              )