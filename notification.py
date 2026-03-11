import datetime
import time
from plyer import notification


while True:
    notification.notify(
        title=" to- do list ".format(datetime.date.today()),
        message=" 1. Live Classes  \n 2. projects  \n presentation ",
        app_icon="./assets/icon.ico",
        timeout=5,
    )
    time.sleep(60*60*4)