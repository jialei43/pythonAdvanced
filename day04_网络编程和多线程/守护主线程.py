'''
演示守护线程
'''
import threading
import time


def work():
    for i in range(10):
        print('working....')
        time.sleep(0.2)


if __name__ == '__main__':
    # daemon=True：主线程退出时，子线程自动结束
    threading.Thread(target=work, daemon=True).start()
    time.sleep(1)
    print('主线程执行完毕')