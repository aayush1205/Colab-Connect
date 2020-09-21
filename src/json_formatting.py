import json
import os

x = os.getcwd()
x = x.split('/')
root = x[1]     
name = x[2]
Flag = False
os.chdir('/'+root+'/'+name+'/.config/Code/User')


def make_json():
    with open("keybindings.json","r") as f:
        data = f.read().split()
        if ("[]") in data:
            return None
        if ('[') and (']') not in data:
            print('Modifying json')
            with open("keybindings.json","a") as fout:
                fout.write('[]')




with open('keybindings.json',"r+")  as f:
    for i in f:
        if i.startswith('/'): 
            Flag = True

if Flag:
    with open('keybindings.json', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('keybindings.json', 'w') as fout:
        fout.writelines(data[1:])
    
Flag = False

def write_json(data):
    with open('keybindings.json',"w") as json_file:
        json.dump(data,json_file,indent=4)


if not Flag:
    with open('keybindings.json') as file:
        make_json()
        file = file.read()
        data = json.loads(file)
        y = {"key":"ctrl+shift+f8","command":"opensshremotes.openEmptyWindow","when":"isLinux"} 
        data.append(y)
        write_json(data)