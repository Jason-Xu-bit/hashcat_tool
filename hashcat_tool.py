from os import system
from module.opfile import opfiles
from module.color import *

file_path = ()  # hashcat文件路径
dic_path = ()  # 字典文件路径
dic_cmd = ''  # 格式化的字典命令
w = ''  # 性能

ErrP('w', '请将本程序放在hashcat目录下')
ErrP('i', '可多选文件')

file_path = opfiles(title='打开hashcat文件')  # 读取hashcat文件
dic_path = opfiles(title='打开字典文件')  # 读取字典文件

for i in range(len(dic_path)):
    dic_cmd = dic_cmd + ' ' + dic_path[i]

w = input('性能(1-4)>')

if input('是否在字典破解完成后开始8位数字暴力破解(默认:y/n)>') == 'n':
    for i in range(len(file_path)):  # 破解命令
        ErrP('p', '\n===============' + '[' + str(i + 1) + '/' + str(len(file_path)) + '] ' + file_path[i].split('/')[-1] + ' [字典破解]===============')  # 进度
        ErrP('g', 'hashcat -m 22000 -w ' + w + ' ' + file_path[i] + ' ' + dic_cmd)
        system('hashcat -m 22000 -w ' + w + ' ' + file_path[i] + ' ' + dic_cmd)
else:
    for i in range(len(file_path)):  # 破解命令
        ErrP('p', '\n===============' + '[' + str(i + 1) + '/' + str(len(file_path)) + '] ' + file_path[i].split('/')[-1] + ' [字典破解]===============')  # 进度
        ErrP('g', 'hashcat -m 22000 -w ' + w + ' ' + file_path[i] + ' ' + dic_cmd)
        system('hashcat -m 22000 -w ' + w + ' ' + file_path[i] + ' ' + dic_cmd)
        ErrP('p', '\n===============' + '[' + str(i + 1) + '/' + str(len(file_path)) + '] ' + file_path[i].split('/')[-1] + ' [暴力破解]===============')  # 进度
        ErrP('g', 'hashcat -a 3 -m 22000 -w ' + w + ' ' + file_path[i] + ' ?d?d?d?d?d?d?d?d')
        system('hashcat -a 3 -m 22000 -w ' + w + ' ' + file_path[i] + ' ?d?d?d?d?d?d?d?d')
