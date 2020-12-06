from math import sqrt
def car():
    for x in range(1,10):
        for y in range(1,10):
            a=x*1100+y*11
            b=int(sqrt(a))
            if b*b==a:
                print("撞人车辆是：陕A",a)
def zijie():
    he=0
    wen=open("D:\\justin\\courses for LZY.txt",encoding="utf8")#wen=open("D:\\justin\\courses for LZY.txt",encoding="utf8")
    jian=wen.read()
    print(len(jian))
    wen.close()
    wen=open("D:\\justin\\courses for LZY.txt",encoding="utf8")
    jian=len(wen.readlines())
    print(jian)
    wen.close()
    wen=open("D:\\justin\\courses for LZY.txt",encoding="utf8")
    jian=wen.readlines()
    for line in jian:
        he=he+len(line)
    print(he)
    wen.close()
def wanmei():
    for x in range(100,1000):
        a=int(x/100)
        b=int((x-a*100)/10)
        c=int(x-a*100-b*10)
        if a*a*a+b*b*b+c*c*c==x:
            print(x)
def lirun():
    money=(float(input("How much money?")))
    if money<=100000:
        returns=downten(money)
        print(returns)
    elif 100000<money<=200000:
        returns=downtwe(money)
        print(returns)
    elif 200000<money<=400000:
        returns=downfor(money)
        print(returns)
    elif 400000<money<=600000:
        returns=downsix(money)
        print(returns)
    elif 600000<money<=1000000:
        returns=downhun(money)
        print(returns)
    else:
        returns=uphundr(money)
        print(returns)
    
def downten(money):
    returns=money/10
    return returns
def downtwe(money):
    returns=downten(100000)+((money-100000)/100*7.5)
    return returns
def downfor(money):
    returns=downtwe(200000)+((money-200000)/100*5)
    return returns
def downsix(money):
    returns=downfor(400000)+((money-400000)/100*3)
    return returns
def downhun(money):
    returns=downsix(600000)+((money-600000)/100*1.5)
    return returns
def uphundr(money):
    returns=downhun(1000000)+((money-1000000)/100*1)
    return returns
def water():
    a,b,c,d=0,0,0,0
    for x in range(1000,10000):
        a=int(x/1000)
        b=int((x-a*1000)/100)
        c=int((x-a*1000-b*100)/10)
        d=int(x-a*1000-b*100-c*10)
        if a*a*a*a+b*b*b*b+c*c*c*c+d*d*d*d==x:#if a^4+b^4+c^4+d^4==x:#if a**4+b**4+c**4+d**4==x:
            print(x)
def jump():
    gao=int(input("起始高度："))
    ci=int(input("弹跳次数："))
    zong=0
    for x in range(ci):
        zong=zong+gao
        gao=gao/10*6
        zong=zong+gao
    print(zong)
if __name__=="__main__":
    jump()
    car()
    zijie()
    wanmei()
    water()
    lirun()
