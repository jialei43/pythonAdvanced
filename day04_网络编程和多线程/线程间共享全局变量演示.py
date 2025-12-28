import threading
import time

my_list = []
def writer():
    for e in range(10):
        my_list.append(e)

def read():
    print(f'read：{my_list}')

if __name__ == '__main__':
    t=threading.Thread(target=writer)
    t2=threading.Thread(target=read)
    t.start()
    time.sleep(1)
    t2.start()