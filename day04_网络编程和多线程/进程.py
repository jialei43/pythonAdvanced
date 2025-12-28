from multiprocessing import Process
value = 0
def add_num():
    global value
    for e in range(100000):
        value += e



if __name__ == '__main__':

    p = Process(target=add_num,args=())
    p2 = Process(target=add_num,args=())
    p.start()
    p2.start()
    print(value)