
#文件的打开、读写、关闭
'''
1、文件打开
file_obj=open(filename,mode='r',buffering=-1,0,...)  encoding=...
打开形式：
二进制文件可以不使用缓冲，但是文本文件必须使用
打开模式：
r读  w写(清空原内容)  a追加：文件尾部追加内容
x  以写模式打开，若文件已存在则失败
r+ = r+w以读写模式打开
w+ = w+r以读写模式打开（清空原内容） 
a+ = a+r以读和追加模式打开 
后面加b就表示二进制文件的读、写、追加
rb（以二进制读模式打开）  wb  ab
rb+  wb+  ab+
'''
#新建文件，并写入
'''
with open(r'd:\pythonstudy\firstpro.txt','w') as f:
    f.write('Hello world!')
'''
#with语句再执行之后会主动关闭文件句柄
'''
with open(r'd:\pythonstudy\firstpro.txt') as f:
    p1=f.read(5)
    p2=f.read()
    print(p1)
    print(p2)
'''

#读写多行数据
'''
readlines()返回一个列表
readline()
writelines()

'''
'''
with open(r'd:\pythonstudy\fzy.txt') as f1:
    p1=f1.readlines()
print(p1)
for i in range(0,len(p1)):
    p1[i]=str(i+1)+' '+p1[i]
with open(r'd:\pythonstudy\zhiyingf.txt','w')as f2:
    p2=f2.writelines(p1)
    
print(p1)
'''

#文件指针 数据读写都有一个文件指针
#seek(offset,whence=0)在文件中移动文件指针，从whence（0表示文件头部，1表示当前位置，2表示文件尾部）偏移offset个字节
'''
s='Tencent Technology Company Limited.'
with open(r'd:\pythonstudy\zhiyingf.txt','a+') as f:
    f.writelines('\n') 
    f.writelines(s)
    f.seek(0)
    cNames=f.readlines()
print(cNames)
'''

#
'''
stdin标准输入
stdout
stderr
'''

#综合使用一下
'''
import os
def countLines(fname):
    try:
        with open(fname) as f:
            data=f.readlines()
    except FileNotFoundError:
        print(fname+'does not exist.')
    lens=len(data)
    print(fname+' has '+str(lens)+' lines')
files=['data1.txt','data2.txt','data3.txt','data4.txt']

os.chdir(r'd:\pythonstudy\workdir')
for fname in files:
    s=input('Please input a str:')
    with open(fname,'w')as f:
            f.writelines(s)
for fname in files:
    countLines(fname)
'''

#
import os
import shutil
def countLines(fname):
    try:
        with open(fname) as f:
            data=f.readlines()
    except FileNotFoundError:
        print(fname+'does not exit.')
    lens=len(data)
    print(fname.split('\\')[1]+' has ' + str(lens)+ ' lines')
path='./workdir'#./表示当前目录   ../表示回到上一级目录
os.chdir(r'd:\pythonstudy')
for fname in os.listdir(path):
    if fname.endswith('.txt'):#文件以.txt结尾
        file_path=os.path.join(path,fname)
        countLines(file_path)

    if os.path.exists('./output'):
        shutil.rmtree('./output')#rmtree递归的删除目录
    os.mkdir('./output')#mkdir用于创建目录
    
