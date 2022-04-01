from time import sleep
from os import system



def progress1():
	system('mode con:cols=120 lines=30')
	out=''
	for i in range(101):
		out='进度 ['+'#'*i+' '*(100-i)+'] '+str(i)+'%'
		print('\r'+out,end=' ',flush=True)
		sleep(0.03)
	print('完成\a',end='\n')


def progress2():
	system('mode con:cols=120 lines=30')
	out=''
	p=['-','\\','|','/','-']
	t=0
	for i in range(101):
		out=' '+p[t]+' 进度 ['+'#'*i+' '*(100-i)+'] '+str(i)+'%'
		print('\r'+out,end=' ',flush=True)
		sleep(0.04)   #时间可调
		if i%2==0:   #当进度为3的倍数时转一下 可调
			t=t+1
		if t==4:
			t=0
	print('完成\a',end='\n')


def loading():
	for i in range(3):   #while True:
		print('Loading',end='')
		for i in range(3):   #3为点的个数
			print('.',end='',flush=True)
			sleep(1)   #等待的秒数
		print('\r'+' '*10+'\r',end='')   #*后面的数字=点的个数+7 (7指的是Loading)


def exit1():
	print('即将退出',end='',flush=True)
	for i in range(3):
		print('.',end='',flush=True)
		sleep(1)
	exit()


def exit2():
	for i in range(3,0,-1):
		print('\r即将退出:-'+str(i)+'-',end='',flush=True)
		sleep(1)
	exit()

def WaitP(mess,sec):
	print(mess,end='')
	for i in range(sec):   #3为点的个数
		print('.',end='',flush=True)
		sleep(0.5)   #等待的秒数
	print('\r'+' '*(len(mess)*2+sec)+'\r',end='')   #*后面的数字=点的个数+7 (7指的是Loading)
	system('cls')

