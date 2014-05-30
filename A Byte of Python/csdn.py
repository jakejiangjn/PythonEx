#!/usr/bin/python
#coding=utf-8       # 如果脚本中有中文 #coding=gbk 或者 utf-8，不然提示错误
# Filename: csdn.py

import  sys, os
if len(sys.argv) != 3 :   # 如果命令行参数不是三个 比如 csdn.py 88888 pw.txt
    c = raw_input('search:')   # 输入搜索关键字
    d = raw_input('output:')   # 输入输出文件
else:
    c = sys.argv[1]
    d = sys.argv[2]
fr = open('C:/temp/www.csdn.net.sql', 'r')   # 只读打开数数据文件
fw = open(d,'w')                               # 打开输出文件
l = 0                                         # 计数器
for line in open('C:/temp/www.csdn.net.sql'): # 遍历每一行在输入文件里
    line = fr.readline()       # 读取一行到line里
    if line.find(c) != -1:     # line里能否找到 搜索关键字
        l+=1
        print '[' + str(l) + '] ' + line
        fw.write(line)         # 搜到的写到输出文件
fr.close()   # 关闭文件 输入和输出文件
fw.close()
c = raw_input('Done')   # 按任意键结束

#
# coding=gbk
#!/usr/bin/python
# Filename: addline.py

f = open('addline.py' , 'r+') # 打开文件读写
ftext = f.read()              # 读整个文件

f.seek(0)                     # 移到文件头
f.write("# coding=gbk  中文，需要在第一行添加  coding=gbk  或者 coding=utf-8 \n") # 添加一行
f.write(ftext)                # 写回文件
