"""print("hello,word")"""
"""
print(233)
print(2.33)
print(True)
print(())
print([])
print({})

"""
"""
喜喜
a
"""
"""print(1+2>4)"""
# python默认为字符串,当出现连接符+号时:为拼接状态 
# 长的像的数据才能转换
# a= float(input("请输入:"))
# b= float(input("请输入:"))
# print("input获取的内容: ",a+b)


"""a="asasasadsakhbdahvcdukvckdsjvhcjsdhv"
print(len(a))"""

# a=input("请输入: ")
# b=input("请输入: ")
# print(len(a)+len(b))

# list1=['1','2','3','4']
# list1.insert(0,'9')
# print(list1)
# list1.pop(-2)
# print(list1)
# list1.extend("abcddddddddddd")
# print(list1)
# # list1.remove("a")
# # print(list1)
# # list1.sort()
# # print(list1)
# print(list1.count('d'))
# list1.remove('d')
# print(list1)


# a=['1','1','3','4','2']
# print(a.index("1"))
# print (a.count("1"))
# print(a[-3])
# print(a[0:6])
# b=("1","2","3","true","flase")
# print(b.index("2"))
# d=tuple(a)
# c=(a,"1","2","3","true","flase")
# print(c[0][2])
# print(c[-4:-1 ])
# 切片为取值为左闭右开  闭为取值,右为不取

name=input("请输入您的姓名:")

age=input("请输入您的年龄:")

sex=input("请输入您的性别:")
dict1= {}
# dict1.update(姓名=name,年龄=age,性别=sex)
dict1["name"]=name
dict1["age"]=age
dict1["sex"]=sex
print(dict1.keys())
print(dict1.items())
del dict1['name']
print(dict1)
# dict1.clear()
# print(dict1)
d=dict1.pop('age')
print(dict1,d)


 