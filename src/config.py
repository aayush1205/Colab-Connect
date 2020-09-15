import webbrowser
import time
import os.path
from os import path



def configure():

    print("Please paste your unique authtoken by following (Ctrl+Click) :", end=' ')
    text = "this link"
    target = "https://dashboard.ngrok.com/auth/your-authtoken"
    print(f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\")
    var = input("Enter unique Authtoken: " )
    f = open("authkey.txt" , "w+")
    f.write(var)
    print("\n")
    return 
    