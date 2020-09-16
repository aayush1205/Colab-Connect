import json
import os
x = os.getcwd()
x = x.split('/')
root = x[1]      ## generalization 
name = x[2]
os.chdir('/'+root+'/'+name+'/.config/Code/User')