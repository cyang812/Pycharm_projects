import re
BOUNDARY = u"==========\n"
TWOBOUNDARY = u"==========\n==========\n"

#主函数，目前可实现利用关键词进行简单的分割成列表。
f = open("source.txt", "r", encoding='utf-8')
content = f.read()  # 读取全部内容
content = content.replace(u'\ufeff', u'') #替换书名前的空格
#content = content.replace(TWOBOUNDARY,BOUNDARY)
#print(content)
clips = content.split(BOUNDARY)
print("列表个数：",clips.__len__()) # 获取列表的个数
# for i in range(0,4):
#     print(clips[i])
sum = clips.__len__()
print(sum)

# 获取书名存储为列表books，获取除书名外的内容为sentence
both = []
books = []
sentence = []
for i in range(0,sum):
    book = clips[i].split("\n-")
    both.append(book)
    print(book)
    if (book!=['']): # 如果书名为空
        books.append(book[0])
        sentence.append(book[1])
#print(both)
#print(sentence)
#print(books.__len__())
#print(sentence.__len__())

# 处理sentence列表
# time = [] #未处理
# date = [] #处理1
# word = [] #处理2
# mark = [] #结果
# for i in range(0,sentence.__len__()):
#     time = sentence[i].split("于 ")
#     print(time[1])
#     date.append(time[1])
#     for j in range(0,date.__len__()):
#          word = date[j].split("\n\n")
#          if (word!=['']):
#          #    print(word[0])
#             mark.append(word[0])
# print(mark)
# print(mark.__len__())
# print(word)
# print(word.__len__())

# 去除书名列表中的重复元素
nameOfBooks = list(set(books))
nameOfBooks.sort(key=books.index)
#print(nameOfBooks)
#print(nameOfBooks.__len__()) # 书名的总数
#print(nameOfBooks.count(""))

# 根据不同书名建立字典，字典值为列表
books_dict = {}
for j in range(0,nameOfBooks.__len__()):
    books_dict [nameOfBooks[j]] = []
#print("\n字典长度：",len(books_dict))
#print(books_dict[nameOfBooks[1]])

# 添加字典的内容 （构建一个一对多的数据结构）
temp = []
change = []
for j in range(0,sentence.__len__()):
    temp = both[j]
    #print(temp)
    change = books_dict[temp[0]]
    print(change)
    if (temp[0] in books_dict): # 检索字典
        print("true")
        #change.append[temp[1]]
print(books_dict)
print(len(books_dict))
