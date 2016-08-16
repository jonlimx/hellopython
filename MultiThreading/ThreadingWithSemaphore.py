import threading
import time

def worker(n, sema):
    # Wait to be signalled
    sema.acquire()

    # Do some work
    print('Working', n)


if __name__ == '__main__':
    sema = threading.Semaphore(value=2)
    n_Workers = 10
    for n in range(10):
        t = threading.Thread(target=worker, args=(n, sema))
        t.start()

    for n in range(10):
        time.sleep(5)
        sema.release()

