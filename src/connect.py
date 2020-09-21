import os
import time
import sys
import os.path
from os import path
from press import open_serv
from config import configure
from colorama import Fore


x = os.getcwd()
x = x.split('/')
root = x[1]     
name = x[2]
confpath = '/'+root+'/'+name+'/.ssh/config'

sform = '''

	Host google_colab_ssh
		HostName something
		User root
		Port 0000
'''


def collect():

    f = open("authkey.txt" , "r")
    token = f.read()
    scode = '''

    !pip install colab_ssh --upgrade
    from colab_ssh import launch_ssh, init_git
    password = "colab"
    launch_ssh("{ngrokToken}",password)

    '''.format(ngrokToken = token)
    

    print("(Ctrl+Click) ", end=' ')
    text = "this link"
    target = "https://colab.research.google.com/#create=true"
    print(Fore.BLUE + f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\", end = ' ' + Fore.RESET)
    print(Fore.MAGENTA + " select the desired runtime type, and paste the output of the following code : " + Fore.RESET)
    print("\n")
    print(Fore.RED + scode + Fore.RESET)
    print("\n")
    print("The output will be of the following format: ")
    print(Fore.RED + sform + Fore.RESET)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    f = open(confpath, "w+")
    f.write(text)
    f.close()

def connect():

    if not path.exists("authkey.txt"):
        print("\n")
        configure()

    collect()
    os.system("code")
    time.sleep(3)
    open_serv()
    
    sys.exit()







