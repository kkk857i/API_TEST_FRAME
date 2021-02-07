# -*- coding:utf-8 -*-

import ast
sum=eval('3+5')
print(sum)

print(ast.literal_eval(("{'name':'linux','age':'18'}")))

print(eval("{'name':num,'age':'13'}",{"num":18}))

age=10
print(eval("{'name':'linux','age':age}",{"age":18},locals()))

eval("__import__('os').system('ls')")