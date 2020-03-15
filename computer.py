a=input("运算符号是什么？：")
if a=="+":
    b=float(input("哪个数在前？："))
    c=float(input("哪个数在后？："))
    d=b+c
    print(d)
elif a=="-":
    b=float(input("哪个是被减数？："))
    c=float(input("哪个是减数？："))
    d=b-c
    print(d)
elif a=="*":
    b=float(input("哪个数在前？："))
    c=float(input("哪个数在后？："))
    d=b*c
    print(d)
elif a=="/":
    b=float(input("哪个是被除数？："))
    c=float(input("哪个是除数？："))
    d=b/c
    print(d)
else:
    print("很抱歉，没有这个运算符号。")
