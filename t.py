#coding=utf-8

from langconv import *
 
# 转换繁体到简体
line = "憂鬱的烏龜"

line = Converter('zh-hans').convert(line.decode('utf-8'))
line = line.encode('utf-8')

print line
