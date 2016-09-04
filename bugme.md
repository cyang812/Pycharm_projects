# Bugme


## bug1

Q: `UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 18: illegal multibyte sequence`

S：在打开是指定编码类型，如下：
`f = open("foo.txt", "r", encoding='utf-8')`

## bug2
Q: 去除列表的重复元素

S:
```python
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print l2
```

## bug3
Q:如何输出空格

S:`\0`

## bug4
Q:以变量的名字创建带后缀的文件

E:
```python
//以str1变量命名文件名

//错误方法：不能用引号把变量引用
output=open("str1.txt",'w')
//结果为str1.txt，故该方法错误
 ```

S:
``` python
//正确方法：用+号连接符连接后缀名
ouput=open(str1+".txt",'w')
//用引号括起来表示的是字符串常量，不在引号中才表示变量
//注：如果是在windows下运行，变量str1中不能有在文件名中不能出现的特殊字符
```
