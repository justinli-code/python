def guizong(money):
    if money<=100000:
        returns=downten(money)
        return returns
    elif 100000<money<=200000:
        returns=downtwe(money)
        return returns
    elif 200000<money<=400000:
        returns=downfor(money)
        return returns
    elif 400000<money<=600000:
        returns=downsix(money)
        return returns
    elif 600000<money<=1000000:
        returns=downhun(money)
        return returns
    else:
        returns=uphundr(money)
        return returns
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
if __name__=="__main__":
    money=(float(input("How much money?")))
    print(guizong(money))