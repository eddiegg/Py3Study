import multiprocessing
import threading
from time import sleep, ctime


def music():
    for i in range(3):
        print('listenin music...'+ctime())
        sleep(4)

def movie():
    for i in range(2):
        print('watching movie...'+ctime())
        sleep(10)

threads =[]
t1=multiprocessing.Process(target=music)
t2=multiprocessing.Process(target=movie)
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("finished")
    print(ctime())
