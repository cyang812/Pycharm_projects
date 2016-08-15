list = []

for j in range(3):
    i = int(input())
    list.append(i)#向列表中添加一个元素
    list.sort()#将列表从小到大排序
    #list.sort(reverse=True)#将列表从大到小排序

print(list)