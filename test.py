# from win11toast import toast, notify
# from win10toast import ToastNotifier
# from winotify import Notification
from plyer import notification
import pyautogui as pag


page = pag.getActiveWindow().title.split(' - ')[-1]

# toast("Page set to", page)


# toaster = ToastNotifier()
# toaster.show_toast("Page set to", page, icon_path="./images/icon.ico", duration=3)


# x
# toast = Notification(
#     app_id="Auto Saver",
#     title="Page set to",
#     msg=page,
#     icon="./images/icon.ico",
#     duration='short'
# )

# toast.show()    

notification.notify(
    app_name="Auto Saver",
    title="Page set to",
    message=page,
    app_icon="./images/icon.ico",
    timeout=3
)