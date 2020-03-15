a=input("算什么？：")
if a=="求和":
    b=int(input("首项？："))
    c=int(input("末项？："))
    d=int(input("项数？："))
    e=(b+c)*d/2
    print(e)
elif a=="首项":
    b=int(input("末项？："))
    c=int(input("项数？："))
    d=int(input("公差？："))
    e=b-(c-1)*d
    print(e)
elif a=="末项":
    b=int(input("首项？："))
    c=int(input("项数？："))
    d=int(input("公差？："))
    e=b+(c-1)*d
    print(e)
elif a=="项数":
    b=int(input("首项？："))
    c=int(input("末项？："))
    d=int(input("公差？："))
    e=(c-b)/d+1
    print(e)
else:
    print("考试不会出求这个的！")
