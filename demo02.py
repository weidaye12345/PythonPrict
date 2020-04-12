#判断的print必须以4个空格隔开
height=float(input('请输入您的身高:'))
weight=float(input('请输入您的体重:'))
BMI=weight/height**2
print("您的BMI值为: %.2f"%BMI)
if BMI<18.5:
    print("你的体重太轻了")
elif BMI<25:
    print("正常体重")
elif BMI<28:
    print("过重")
elif BMI<32:
    print("肥胖")
elif BMI>32:
    print("严重肥胖")