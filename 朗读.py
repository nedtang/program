import math
from aip import AipSpeech
import tkinter as tk
from tkinter import filedialog

root=tk.Tk()

root.withdraw()

""" 你的 APPID AK SK """
APP_ID = '14636839'
API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
Filepath=filedialog.askopenfilename()
with open(Filepath,'r') as f:

    content=f.read()
result=b''
for i in range(0,math.ceil(len(content)/300)):

    result += client.synthesis(content[300*i:300*(i+1)], 'zh', 2, {'vol': 7,})

if not isinstance(result, dict):
    file=input("请输入生成文件名称：")
    with open(file+'.mp3', 'wb') as f:
        f.write(result)



