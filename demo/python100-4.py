#python练习题100-2 计算利润
'''
输入三个整数x,y,z，请把这三个数由小到大输出
'''
year = int(input('请输入年'))
month = int(input('请输入月'))
day = int(input('请输入日'))
r = 0
#方法一
#1,3,5,7,8,10,12 每个月都是31天。
months = [0,31,59,90,120,151,181,212,242,273,304,334]
if(month>0 and month<=12):
    r = months[month-1]
else:
    print('data error')
r += day
def isleap(y): #判断是否是闰年
    return y%4==0 and (y%100!=0 or y%400 ==0)
if isleap(year) and month > 2:
    r+=1
print('It\'s the %ddays'%r)













