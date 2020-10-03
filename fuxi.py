def jia(a,c):
    d=a+c
    return d
def jian(a,c):
    d=a-c
    return d
def cheng(a,c):
    d=a*c
    return d
def chu(a,c):
    d=a/c
    return d

print("尊敬的用户们，本计算机使用方法如下：先输入第一个数(如被减数、被除数)，按下”ENTER“再输入运算符，按下”ENTER“最后输入剩下的数，按下”ENTER“")
a= float(input())
b=input()
c=float(input())
if b == "+":
    d=jia(a,c)
    print(d)
elif b == "-":
    d=jian(a,c)
    print(d)
elif b == "*":
    d=cheng(a,c)
    print(d)
elif b =="/":
    d=chu(a,c)
    print(d)
else:
    print("对不起，不支持此类运算(-_-”)")