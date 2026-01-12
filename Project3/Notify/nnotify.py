# import os
# import time
# from plyer import notification

# if __name__=="__main__":
# # while True:
# # time.sleep(10)
#     notification.notify(title="water",message="take a sip of water",timeout=3)
#     time.sleep(10)


import time
from plyer import notification

def send_notification():
    notification.notify(
        title="💧 Time to Take a Break!",
        message="Stretch your legs and drink some water.",
        timeout=5
    )

if __name__ == "__main__":
    interval = 60 * 20  # 20 minutes
    try:
        while True:
            send_notification()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Notification loop exited.")
