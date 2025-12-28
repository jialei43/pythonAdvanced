import threading
from multiprocessing import Process, Value

g_num =0

def sum_num1():
    global g_num
    for e in range(100000000):
        g_num = g_num + 1
    print(f'sum1的值：{g_num}')

def sum_num2():
    global g_num
    for e in range(100000000):
        g_num = g_num + 1
    print(f'sum2的值：{g_num}')

def sum_num3(v):
    for e in range(100000):
        v.value+=1

if __name__ == '__main__':
    # t1=threading.Thread(target=sum_num1)
    # t2=threading.Thread(target=sum_num2)
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()
#     为了实现预期效果

    v = Value('i',0)
    # 进程
    p1 = Process(target=sum_num3, args = (v,))
    p2 = Process(target=sum_num3, args = (v,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(v.value)

"""
在Python中，进程和线程虽然在代码执行上有些相似（都可以实现并发执行），但它们有本质的区别，尤其是在资源管理和执行方式上。
进程（Process）与线程（Thread）的主要区别：


内存空间：


进程是操作系统分配资源的基本单位，每个进程都有自己的独立内存空间，彼此之间的数据是隔离的。如果一个进程崩溃，通常不会影响其他进程。


线程是进程中的执行单位，一个进程可以有多个线程。所有线程共享进程的内存空间，因此它们可以共享数据（这是线程间通信的一个优势）。




资源占用：


启动一个进程需要较多的资源（例如内存），因为每个进程需要独立的内存空间。


启动一个线程比进程轻量得多，开销较小，因为线程共享进程的资源。




执行和并发：


进程可以实现真正的并行（如果有多核CPU），因为不同的进程在不同的CPU核心上运行。


线程的并发执行受限于全局解释器锁（GIL）。在Python中，GIL限制了同一时刻只能有一个线程在解释器中执行Python字节码。因此，Python中的线程更适用于I/O密集型任务，而非CPU密集型任务。如果是CPU密集型，进程会更有效。




通信方式：


进程间通信（IPC）：由于进程之间内存隔离，它们通常使用某些机制（如队列、管道、共享内存、文件、socket等）来进行通信。


线程间通信：线程共享同一进程的内存空间，所以它们可以直接访问共享数据，通信相对简便。但这也意味着需要特别小心同步问题，避免数据竞争和死锁。




崩溃的影响：


如果一个进程崩溃，它不会直接影响到其他进程（操作系统会处理崩溃的进程，其他进程继续运行）。


如果一个线程崩溃，可能会影响整个进程，因为它们共享内存，崩溃的线程可能会破坏进程内的其他资源。




使用场景：


进程适用于：


CPU密集型任务（例如计算、大量数据处理）。


当需要确保任务的隔离，避免共享内存等资源时（例如不同用户的应用）。


使用多核CPU时，可以充分利用多核优势。




线程适用于：


I/O密集型任务（例如文件操作、网络请求等），因为在I/O操作时，Python的线程可以在等待I/O时切换到其他线程执行。


需要轻量级并发，避免创建过多进程的资源浪费时。




总结：


进程适合需要独立内存空间、需要隔离执行环境、或者CPU密集型的任务。


线程适合需要共享内存空间、需要轻量级并发、或者I/O密集型的任务。


Python的threading库适合I/O密集型并发，multiprocessing库更适合CPU密集型并行处理。
希望这个解释能帮你理清它们之间的区别！
"""



