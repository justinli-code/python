import random#引进ranmdom库
def zdaozhi(shu):
    if len(shu)<2:
        return shu
    else:
        return zdaozhi(shu[1:])+shu[0]
def daozhi(shu):
    if len(shu)<2:
        return shu
    else:
        return daozhi(shu[1:])+[shu[0]]
def qushu(shu):
    """
    求列表中有几个元素，效果等同于”len()“
    """
    if len(shu)==0:#基线条件
        return 0
    else:#递归条件
        return qushu(shu[1:])+1
def qiuhe(shu):
    """
    求列表中所有元素的和
    """
    if len(shu)==0:#基线条件
        return 0
    else:#递归条件
        return shu[0]+qiuhe(shu[1:])
def paixu(shu):
    """
    将列表中的所有元素从小到大排序
    """
    if len(shu) < 2:#基线条件
        return shu
    else:#递归条件
        ji=shu[0]
        xiao=[]
        da=[]
        for x in shu[1:]:
            if x>=ji:
                da.append(x)
            elif x<ji:
                xiao.append(x)

        return paixu(xiao)+[ji]+paixu(da)
def tdaozhi(shu):
    if len(shu)<2:
        return shu
    else:
        return [shu[len(shu)-1]]+daozhi(shu[:len(shu)-1])
def bijiao(da,shu):
    if len(shu)==1:
        if da>=shu[0]:
            return da
        else:
            return shu[0]
    else:
        if shu[0]>da:
            da=shu[0]
        return bijiao(da,shu[1:])
if __name__=="__main__":
    biao=[]
    fu=0
    for x in range(100):
        fu=random.randint(1,100)
        biao.append(fu)
    print(biao)
    print(paixu(biao))
    print(qiuhe(biao))
    print(qushu(biao))
    print(daozhi(biao))
    print(tdaozhi(biao))
    chuan="abcdefghi"
    print(zdaozhi(chuan))
    shu=0
    print(bijiao(shu,biao))
