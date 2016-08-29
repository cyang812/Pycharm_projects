# Bugme


## bug1

`UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 18: illegal multibyte sequence`

s：在打开是指定编码类型，如下：
`f = open("foo.txt", "r", encoding='utf-8')`
