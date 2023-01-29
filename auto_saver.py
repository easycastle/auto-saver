import pystray
import PIL.Image
from plyer import notification

import pyautogui as pag
import keyboard
import threading


key = ['ctrl', 's']
interval = 4
page = None
saveThread = None
ableNotification = True


def set_page(icon, item):
    global page

    pag.hotkey('alt', 'tab')
    page = pag.getActiveWindow().title.split(' - ')[-1]

    notification.notify(
        app_name='Auto Saver',
        title='Page set to',
        message=page,
        app_icon='./images/icon.ico',
        timeout=5
    )

def save():
    global key, saveThread
    
    if page == None:
        pag.alert('Please set page first', 'Error')
        return

    else:
        if page != pag.getActiveWindow().title.split(' - ')[-1]:
            return

        pag.hotkey(*key)
        saveThread = threading.Timer(interval, save)
        saveThread.start()

def on_clcik_start(icon, item):
    save()

def on_click_change_key(icon, item):
    global key

    key.clear()
    key = keyboard.read_hotkey().split('+')
    isKeyRight = pag.confirm('Is this key right? ' + '+'.join(key), 'Change Key', ['Yes', 'No'])

    while isKeyRight != 'Yes':
        key.clear()
        key = keyboard.read_hotkey().split('+')
        isKeyRight = pag.confirm('Is this key right? ' + '+'.join(key), 'Change Key', ['Yes', 'No'])

def on_click_change_interval(icon, item):
    global interval

    while True:
        try:
            interval = int(pag.prompt('Enter interval', 'Change Interval'))
        except ValueError:
            pag.alert('Please enter a number', 'Change Interval')
        else:
            break

# def on_click_enable_disable_notification(icon, item):
#     global ableNotification

#     if ableNotification:
#         ableNotification = False
#     else:
#         ableNotification = True
#         # notification.notify(
#         #     app_name='Auto Saver',
#         #     title='Notification',
#         #     message='Notification is enabled',
#         #     app_icon='./images/icon.ico',
#         #     timeout=3
#         # )

#     print(ableNotification)

def on_clcik_stop(icon, item):
    global saveThread

    saveThread.cancel()

def on_click_exit(icon, item):
    icon.visible = False
    tray.stop()



icon = PIL.Image.open('./images/icon.ico')

tray = pystray.Icon(name='Auto Saver', icon=icon, title='Auto Saver', menu=pystray.Menu(
    pystray.MenuItem('Set Page', set_page),
    pystray.MenuItem('Start', on_clcik_start),
    pystray.MenuItem('Change Key', on_click_change_key),
    pystray.MenuItem('Change Interval', on_click_change_interval),
    # pystray.MenuItem('Enable Notification', on_click_enable_disable_notification, default=not ableNotification, checked=lambda item: not ableNotification, radio=True, visible=True),
    pystray.MenuItem('Stop', on_clcik_stop),
    pystray.MenuItem('Exit', on_click_exit),
))

tray.run()