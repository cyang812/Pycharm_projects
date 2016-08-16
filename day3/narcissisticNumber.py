for i in range(152,1000):
    x = int(i/100)
    y = int((i/10)%10)
    z = int(i%10)
    ans = (x**3)+(y**3)+(z**3)
    if i == ans:
        print(i)
