print("----欢迎进入地铁购票系统----")
print("票价如下：")
print("1、成人票：5.0 RMB/张 \n"
      "2、儿童票：2.5 RMB/张 \n")
num1=int(input('请输入要购买的成人票的数量：'))
num2=int(input('请输入要购买的儿童票的数量：'))
print("请确认成人票数量：",int(num1))
print("请确认儿童票数量：",int(num2))
print("------------------------")
num3=float(num1*5.0)
num4=float(num2*2.5)
sum=num3+num4
print("您需要支付："+str(sum)+" RMB")
print("------------------------")
