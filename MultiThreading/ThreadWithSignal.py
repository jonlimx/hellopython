from threading import Thread, Event
import time

# Code to execute in a independent thread
def countdown(n, started_evt):
    print('Countdown starting...')
    time.sleep(10)
    started_evt.set()
    while n > 0:
        print('Counting down: ', n)
        n -= 1
        time.sleep(2)


if __name__ == '__main__':
    started_evt = Event()
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()
    print('Thread started...')
    started_evt.wait()
    print('Counting down started...')

