import re
BOUNDARY = u"==========\n"

#主函数，目前可实现利用关键词进行简单的分割成列表。
f = open("foo.txt", "r", encoding='utf-8')
content = f.read()  # 读取全部内容
#print(content)
numOfLine = content.find(BOUNDARY)
print(numOfLine)
clips = content.split(BOUNDARY)
print(clips[0])


#for i in (2,numOfLine):
# if numOfLine>0:
#       print(content)

# for line in lines:
#     print(line)

# BOUNDARY = u"==========\r\n"
#
# def get_sections(filename):
#     with open(filename, 'r',encoding='utf-8') as f:
#         content = f.read()
#     content = content.replace(u'\ufeff', u'')
#     return content.split(BOUNDARY)
#
# def get_clip(section):
#     clip = {}
#
#     lines = [l for l in section.split(u'\r\n') if l]
#     if len(lines) != 3:
#         return
#
#     clip['book'] = lines[0]
#     match = re.search(r'(\d+)-\d+', lines[1])
#     if not match:
#         return
#     position = match.group(1)
#
#     clip['position'] = int(position)
#     clip['content'] = lines[2]
#
#     return clip
#
# sections=get_sections("foo.txt")
# for section in sections:
#     print(section)
#     print("================================")
#
