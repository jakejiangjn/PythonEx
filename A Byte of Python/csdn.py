#!/usr/bin/python
#coding=utf-8       # ����ű��������� #coding=gbk ���� utf-8����Ȼ��ʾ����
# Filename: csdn.py

import  sys, os
if len(sys.argv) != 3 :   # ��������в����������� ���� csdn.py 88888 pw.txt
    c = raw_input('search:')   # ���������ؼ���
    d = raw_input('output:')   # ��������ļ�
else:
    c = sys.argv[1]
    d = sys.argv[2]
fr = open('C:/temp/www.csdn.net.sql', 'r')   # ֻ�����������ļ�
fw = open(d,'w')                               # ������ļ�
l = 0                                         # ������
for line in open('C:/temp/www.csdn.net.sql'): # ����ÿһ���������ļ���
    line = fr.readline()       # ��ȡһ�е�line��
    if line.find(c) != -1:     # line���ܷ��ҵ� �����ؼ���
        l+=1
        print '[' + str(l) + '] ' + line
        fw.write(line)         # �ѵ���д������ļ�
fr.close()   # �ر��ļ� ���������ļ�
fw.close()
c = raw_input('Done')   # �����������

#
# coding=gbk
#!/usr/bin/python
# Filename: addline.py

f = open('addline.py' , 'r+') # ���ļ���д
ftext = f.read()              # �������ļ�

f.seek(0)                     # �Ƶ��ļ�ͷ
f.write("# coding=gbk  ���ģ���Ҫ�ڵ�һ�����  coding=gbk  ���� coding=utf-8 \n") # ���һ��
f.write(ftext)                # д���ļ�
