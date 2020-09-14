import time
import requests


def upup(address, n):
    list1 = ['dragon','motto']
    path = 'C:\\Code\\CQP-xiaoi\\酷Q Pro\\data\\image\\'+address+'.cqimg'
    path2 = 'C:\\Code\\CQP-xiaoi\\酷Q Pro\\data\\image\\'+list1[n]+'\\'
    url = ''
    with open(path,'r') as f:
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            if line[:4] == 'url=':
                url = line[4:]
                if len(url)<5:
                    return 'None'
                break
            line = f.readline()
    if not url:
        return
    t = str(int(time.time()))+address[-4:]
    with open(path2+t,'wb+') as f2:
        cont = requests.get(url)
        f2.write(cont.content)
    return url


def urlup(address,url,text):
    path2 = 'C:\\Code\\CQP-xiaoi\\酷Q Pro\\data\\image\\'+text+'\\'
    t = str(int(time.time()))+address[-4:]
    with open(path2+t,'wb+') as f2:
        cont = requests.get(url)
        f2.write(cont.content)
    print("ok")