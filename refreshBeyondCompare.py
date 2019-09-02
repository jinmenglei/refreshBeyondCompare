'''refresh BeyondCompare4 to 28'''
import time
import os  # 引入操作系统模块
import sys  # 用于标准输入输出


def search(path, name):
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1  # 判断是否找到文件
            root = str(root)
            return root
    return -1


path = 'C://Users'
name = 'BCompare.ini'  # 标准输入,其中rstrip()函数把字符串结尾的空白和回车删除
answer = search(path, name)
answer = answer + '\\' + name
if answer == -1:
    print("查无此文件")
    print('再见')
else:
    print(answer)
    f_BC = open(answer,'r+')
    content = f_BC.readlines()
    f_BC.seek(0,0)
    f_BC.truncate()
    time_refresh = str(int(time.time()))
    f_BC.write(content[0])
    f_BC.write(content[1][:12] + time_refresh + "\n")
    f_BC.write(content[2][:12] + time_refresh + "\n")
    f_BC.close()
