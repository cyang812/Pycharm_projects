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
