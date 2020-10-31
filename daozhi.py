import random  #引进random库 


def i():  #创建函数
    """
    确保输入的是一个正整数
    """
    try:
        c=int(input())  #输入值
        if c>0:
            return c
        else:
            print("格式错误❌，请输入一个正整数")
            return i()    
        
    except Exception:
        print("格式错误❌，请输入一个正整数") 
        return i()
        
def intmain():
    randoms=[]  #创建列表
    b=i() 
    print("取的随机数是：") 
    for x in range(b):
        a = int(random.randrange(1,b*10))  #取随机数
        randoms.append(a)  #将取的随机数加入列表
        print(randoms[x])  #打印取的随机数
    print("以上是",b,"个数") 
    d=int(b/2)
    e=b
    for x in range(d):
        e=e-1
        randoms[x], randoms[e] = randoms[e], randoms[x]  #倒置列表
    print("倒置后的数是：")  
    for x in range(b):
        print(randoms[x])  #打印新的列表

if __name__=="__main__":
    intmain()

    