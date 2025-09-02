import psutil

import time


def monitor_system():
    print("cpu is", psutil.cpu_percent())

if __name__ == "__main__":
  while True:
    monitor_system()
    time.sleep(5)