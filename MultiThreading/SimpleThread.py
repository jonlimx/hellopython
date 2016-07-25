import time
from threading import Thread


# Code to execute in an independent thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create and launch a thread
if __name__ == '__main__':
    # Frontend thread. We can wait on this thread on current thread.
    # t = Thread(target=countdown, args=(10,))

    t = Thread(target=countdown, args=(10,), daemon=True)
    t.start()

    # while t.is_alive():
    #     print('Backend treading is still running...')
    #     time.sleep(2)

    time.sleep(4)
    # A backend thread will be terminated while the main thread is terminated.

    print('Done!!!')
