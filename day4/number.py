#统计一个输入的字符串中英文字母、空格、数字和其它字符的个数

str= input()

letters = 0
space = 0
digit = 0
others = 0

for c in str:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1

print(letters,space,digit,others)



