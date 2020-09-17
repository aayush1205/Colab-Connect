import json
import os

x = os.getcwd()
x = x.split('/')
root = x[1]     
name = x[2]
Flag = False
os.chdir('/'+root+'/'+name+'/.config/Code/User')
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
        file = file.read()
        data = json.loads(file)
        y = {"key":"ctrl+shift+f8","command":"opensshremotes.openEmptyWindow","when":"isLinux"} 
        data.append(y)
        write_json(data)
