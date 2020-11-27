from .celery import app
import time


@app.task()
def run_in_10s():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
    print("hello world")
