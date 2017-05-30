import multiprocessing
import threading
import multitasking
from time import sleep, ctime

multitasking.set_engine("process")

def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print('COST: {}'.format(end - start))
    return wrapper

@multitasking.task
@profile
def music():
    print('listenin music...'+ctime())
    sleep(4)

@multitasking.task
@profile
def movie():
    print('watching movie...'+ctime())
    sleep(7)

if __name__ == '__main__':
    for i in range(5):
        music()
        movie()