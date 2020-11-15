import random#引进ranmdom库
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
if __name__=="__main__":
    biao=[]
    fu=0
    for x in range(10):
        fu=random.randint(1,100)
        biao.append(fu)
    print(biao)
    print(paixu(biao))
    print(qiuhe(biao))
    print(qushu(biao))