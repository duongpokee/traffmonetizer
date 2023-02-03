import os, requests, time

def setup():
    os.system('sudo apt update')
    os.system('sudo apt install apt-transport-https ca-certificates curl software-properties-common')
    os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"')
    os.system('sudo apt update')
    os.system('sudo apt install docker-ce')
    os.system('docker pull traffmonetizer/cli:latest')
def sever():
    global sever
    path = os.getcwd()
    filep = os.path.join(path)
    sever = input('Sever: ')
    if sever == '1':
        s1 = requests.get('https://pastebin.com/raw/B1qSiih4', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s1.content)
        print('Lay du lieu thanh cong!')
    elif sever == '2':
        s2 = requests.get('https://pastebin.com/raw/MKvqkc5V', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s2.content)
        print('Lay du lieu thanh cong!')
    elif sever == '3':
        s3 = requests.get('https://pastebin.com/raw/Xp5GE4a0', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s3.content)
        print('Lay du lieu thanh cong!')
    elif sever == '4':
        s4 = requests.get('https://pastebin.com/raw/MGgJtnEb', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s4.content)
        print('Lay du lieu thanh cong!')
    elif sever == '5':
        s5 = requests.get('https://pastebin.com/raw/1vEGufJv', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s5.content)
        print('Lay du lieu thanh cong!')
    elif sever == '6':
        s6 = requests.get('https://pastebin.com/raw/atq0Je1P', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s6.content)
        print('Lay du lieu thanh cong!')
    elif sever == '7':
        s7 = requests.get('https://pastebin.com/raw/0sdjFpXt', allow_redirects=True)
        with open(filep + '/sever.txt','wb') as file2:
            file2.write(s7.content)
        print('Lay du lieu thanh cong!')

setup()
print('SETUP THANH CONG !')
os.system('clear')
print('MODE 1: CHAY NHAP SERVER')
print('MODE 2: CHAY KHONG CAN NHAP SERVER')
mode = input('Mode:')
if mode == '1':
    os.system('clear')
    time.sleep(3)
    os.system('python run1.py')
if mode == '2':
    sever()
    os.system('clear')
    time.sleep(3)
    os.system('python run2.py')
