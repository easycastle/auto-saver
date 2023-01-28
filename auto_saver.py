from tkinter import *
import pystray
import PIL.Image

import pyautogui as pag
import keyboard
import time

key=['ctrl', 's']
interval = 300

def save():
    pag.hotkey(*key)

def on_clcik_start(icon, item):
    save()
    print('completely saved')
    time.sleep(interval)

def on_click_change_key(icon, item):
    print('changed key')

def on_click_change_interval(icon, item):
    print('changed interval')

def on_clcik_stop(icon, item):
    print('stopped')

def on_click_exit(icon, item):
    icon.visible = False
    tray.stop()

icon = PIL.Image.open('./icon.ico')

tray = pystray.Icon(name='Auto Saver', icon=icon, title='Auto Saver', menu=pystray.Menu(
    pystray.MenuItem('Start', on_clcik_start),
    pystray.MenuItem('Change Key', on_click_change_key),
    pystray.MenuItem('Change Interval', on_click_change_interval),
    pystray.MenuItem('Stop', on_clcik_stop),
    pystray.MenuItem('Exit', on_click_exit),
))

tray.run()