#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
# 打开一个文件
f = open("key.txt", "r")
print("文件名: ", f.name)
print("是否已关闭 : ", f.closed)
print("访问模式 : ", f.mode)
print(f.read(10))
print(f.read)
#f.write('Hello, world!')
f.close()
time.sleep(100)
