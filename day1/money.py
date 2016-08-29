a = (100000,200000,400000,600000,1000000)
b = (0.1,0.075,0.05,0.03,0.015,0.001)

input_money = (int)(input("please input money:"))

if input_money<=a[0] and input_money>0:
    ans = input_money*b[0]
    print(ans)

elif input_money<=a[1] and input_money>a[0]:
    ans = (input_money-a[0])*b[1]+a[0]*b[0]
    print(ans)

elif input_money<=a[2] and input_money>a[1]:
    ans = (input_money-a[1])*b[2]+a[1]*b[1]+a[0]*b[0]
    print(ans)

elif input_money<=a[3] and input_money>a[2]:
    ans = (input_money-a[2])*b[3]+a[2]*b[2]+a[1]*b[1]+a[0]*b[0]
    print(ans)

elif input_money<=a[4] and input_money>a[3]:
    ans = (input_money-a[3])*b[4]+a[3]*b[3]+a[2]*b[2]+a[1]*b[1]+a[0]*b[0]
    print(ans)

elif input_money>a[4]:
    ans = (input_money-a[4])*b[5]+a[3]*b[3]+a[2]*b[2]+a[1]*b[1]+a[0]*b[0]
    print(ans)
