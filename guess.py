"""
import random
a = int(random.randrange(1, 100))
flag =True
while flag:
    _number = int(input("your input number:"))

    if(_number > a):
        print('请输入一个小一点的数字!')
    elif(_number < a):
        print('请输入一个大一点的数字！')
    else:
        print('恭喜你,猜对啦！')
        flag =False
"""
from easygui import *
import random

a = int(random.randrange(1, 100))

msgbox("欢迎使用猜数字游戏机(-_-)!")

flag =True

_number  = integerbox('请输入你猜的数字：',title='猜数字游戏')

while flag:
    

    
    if(_number > a):
        msg ='请输入一个小一点的数字!\n'
        _number  = integerbox(msg + '请输入你猜的数字：',title='猜数字游戏')

    elif(_number < a):
        msg='请输入一个大一点的数字!\n'
        _number  = integerbox(msg + '请输入你猜的数字：',title='猜数字游戏')
    else:
        msgbox('恭喜你,猜对啦！')

        flag =False
    
  
