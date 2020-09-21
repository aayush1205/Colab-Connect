import webbrowser
import time
import os.path
from os import path
from colorama import Fore



def configure():

    print("Please paste your unique authtoken by following (Ctrl+Click) :", end=' ')
    text = "this link"
    target = "https://dashboard.ngrok.com/auth/your-authtoken"
    print(Fore.BLUE + f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\" + Fore.RESET)
    var = input("Enter unique Authtoken: " )
    f = open("authkey.txt" , "w+")
    f.write(var)
    print("\n")
    return 
    