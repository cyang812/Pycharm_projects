#判断一个数是否为完全平方数
def isSquareNumber(i):
    a = set()
    k = 1
    for j in range(1,100):
        k = j*j
        a.add(k)
    if (i in a):
        return 1
    else:
        return 0

#main
for i in range(1,50):
    if (isSquareNumber(i+100)):
        if (isSquareNumber(i+268)):
            print(i)