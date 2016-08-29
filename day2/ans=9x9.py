#99乘法表
for i in range(1,10):
    for j in range(1,10):
        ans = i*j
        print(i,"*",j,"=",ans)
    print()#每执行9次之后，输出一个空行
