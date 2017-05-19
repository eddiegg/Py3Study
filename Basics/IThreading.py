import multiprocessing
import threading
from time import sleep, ctime

def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print('COST: {}'.format(end - start))
    return wrapper

@profile
def music():
    print('listenin music...'+ctime())
    sleep(4)

@profile
def movie():
    print('watching movie...'+ctime())
    sleep(7)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    for i in range(4):
        pool.apply_async(music)
    pool.close()
    pool.join()