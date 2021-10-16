from ctypes import *
import ctypes.util
import os
import sys
os.environ['PATH']+=";" + os.getcwd()
import sciter
import win32api
import win32con
if __name__ == '__main__':
    sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    sh=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    w,h=400,300
    x,y = ((sw-w)//2),((sh-h)//2)
    frame = sciter.Window(ismain=True, debug=True,size=(400,300),pos=(x,y))
    frame.setup_debug()
    frame.load_file("res/main.html")
    frame.expand()
    frame.run_app()