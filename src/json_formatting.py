import json
import os
x = os.getcwd()
x = x.split('/')
root = x[1]
name = x[2]
os.chdir('/'+root+'/'+name+'/.config/Code/User')
file = open('keybindings.json','r').read()
json_file = json.loads(file)
keys = []
try:
    for i in range(len(json_file)):
        flag = True
        keys.append(json_file[i]['key'])
except Exception as e:
   flag = False
def checkIfDuplicates(keys):
    ''' Check if given list contains any duplicates '''
    if len(keys) == len(set(keys)):
        return False
    else:
        return True
duplicates = checkIfDuplicates(keys)
if duplicates:
    
