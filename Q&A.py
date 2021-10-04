import csv
import numpy as np
import random
import sys
from playsound2 import playsound
import mp3

file = "wordlist.csv"
with open(file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [row for row in reader]
data = np.array(data)

def playmp3(word):
    mp3.main(word)
    file = 'Speech_US\\' + word + '.mp3'
    playsound(file)

def right():
    playsound('right.mp3')

def wrong():
    playsound('wrong2.wav')

flag = 1
error_flag = 0
mode = int(input('请选择模式（0.混合模式；1.背单词；2.背操作命令）:'))
if mode not in [0,1,2]:
    print('error happened when choosing mode')
    sys.exit(0)

if mode == 0:
    pass
elif mode == 1:
    length = len(data)
    for i in range(length):
        if data[(length-i-1),2] == '1':
            data = np.delete(data,np.s_[length-i-1],axis=0)
        else:
            pass
else:
    length = len(data)
    for i in range(length):
        if data[(length - i-1), 2] == '':
            data = np.delete(data, np.s_[length - i-1], axis=0)
        else:
            pass
num = int(input('How many things you want to memorize?(the total size is %d):'%(int(len(data))-1)))
if num > len(data):
    print('too many')
    sys.exit(0)
tmp = [i + 1 for i in range(len(data) - 1)]
random.shuffle(tmp)
tmp = tmp[:num]
today_data = data[tmp]


while True:
    question = today_data[flag-1]
    # question = data[random.randint(1,len(data)-1)]
    if error_flag > 0:
        answer = input('你的答案：')
    else:
        print('----------------------------------')
        print(question[1])
        answer = input('你的答案：')
    if answer == question[0]:
        print('\033[0;33m%s\033[0m'%'you are right!')
        right()
        if question[2] != '1':
            playmp3(answer)
        flag += 1
        error_flag = 0
    else:
        error_flag += 1
        if error_flag == 1:
            today_data = np.concatenate((today_data,[question]),axis=0)
        if error_flag == 2:
            print('\033[1;31;40m%s\033[0m'%'正确答案是：',question[0])
            error_flag = 0
        print('\033[0;31m%s\033[0m'%'wrong,try again')
        wrong()
        if question[2] != '1':
            playmp3(question[0])
    if flag > len(today_data):
        print('练习结束')
        sys.exit(0)


