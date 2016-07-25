import time
from threading import Thread


class CountdownTask(object):
    def __init__(self, maxcount):
        self.running = True
        self.n = maxcount

    def terminate(self):
        self.running = False

    def countdown(self):
        while self.running and self.n > 0:
            print('Now is ', self.n)
            self.n -= 1
            time.sleep(3)


if __name__ == '__main__':
    c = CountdownTask(10)
    t = Thread(target=c.countdown)
    t.start()
    while t.is_alive():
        print('Waiting countdown thread to finish.')
        time.sleep(1)
        # Terminate the thread by setting c.running to False
        c.terminate()
    print('Done!!!')
