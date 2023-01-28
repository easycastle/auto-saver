from tkinter import *
import pystray
import PIL.Image

import pyautogui as pag
import keyboard
import time, sched, asyncio
import threading


# window = Tk()
# window.title('Auto Saver')
# window.geometry('300x200')
# window.resizable(False, False)





key = ['ctrl', 's']
interval = 4
schedule = sched.scheduler(time.time, time.sleep)
thread = None

def save():
    global thread

    pag.hotkey(*key)
    print('saved')
    thread = threading.Timer(interval, save)
    thread.start()
#     schedule.enter(interval, 1, save, ())
# schedule.enter(interval, 1, save, ())

def on_clcik_start(icon, item):
    # schedule.run()
    save()

def on_click_change_key(icon, item):
    print('changed key')

def on_click_change_interval(icon, item):
    print('changed interval')

def on_clcik_stop(icon, item):
    global thread

    thread.cancel()
    print('stopped')

def on_click_exit(icon, item):
    icon.visible = False
    tray.stop()

icon = PIL.Image.open('./images/icon.ico')

tray = pystray.Icon(name='Auto Saver', icon=icon, title='Auto Saver', menu=pystray.Menu(
    pystray.MenuItem('Start', on_clcik_start),
    pystray.MenuItem('Change Key', on_click_change_key),
    pystray.MenuItem('Change Interval', on_click_change_interval),
    pystray.MenuItem('Stop', on_clcik_stop),
    pystray.MenuItem('Exit', on_click_exit),
))

# thread = threading.Thread(tray.run())
# thread.start()

# window.mainloop()

tray.run()