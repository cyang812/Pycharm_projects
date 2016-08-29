#判断输入的日期是今年的第几天

list=(31,28,31,30,31,30,31,31,30,31,30,31)
ans = 0

theDay = input("please input the day as yyyymmdd:")

yyyy = int(theDay[0:4])
mm = int(theDay[4:6])
dd = int(theDay[6:8])

#判断是否是闰年
i = yyyy%4

#print(yyyy+mm+dd+str(i))

if i == 0:
    if mm >= 3:
        for j in range(0,mm-1):
            ans = ans+list[j]
        ans = ans+dd+1
    else:
        for j in range(0,mm-1):
            ans = ans+list[j]
        ans = ans + dd
else:
    if mm >= 3:
        for j in range(0,mm-1):
            ans = ans+list[j]
        ans = ans+dd
    else:
        for j in range(0,mm-1):
            ans = ans+list[j]
        ans = ans + dd
print(ans)


