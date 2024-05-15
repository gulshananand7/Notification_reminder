import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "it is good for health",
            timeout = 10
        )
        time.sleep(6)