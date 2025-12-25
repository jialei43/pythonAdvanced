"""
在 Python（特别是官方的 CPython 实现）中，引用计数（Reference Counting） 并不是“变相”存在的，
而是实实在在地存储在每一个 Python 对象的**对象头（Object Header）**中。

在堆内存里，无论你的对象是一个简单的整数、字符串，还是复杂的列表，
它的内存布局最前端都包含了一个名为 ob_refcnt 的字段。

在 CPython 的底层 C 语言实现中，所有的对象都继承自 PyObject 结构体。你可以把它想象成每个对象的“固定模版”。


/* CPython 源代码中 PyObject 的定义简化版 */
typedef struct _object {
    _PyObject_HEAD_EXTRA    // 双向链表指针（仅在调试模式下存在）
    Py_ssize_t ob_refcnt;   // <--- 这就是引用计数存放的地方！
    struct _typeobject *ob_type; // 指向对象类型（如 int, list）的指针
} PyObject;

物理位置：它位于对象在堆内存起始位置的偏移量处。

占据空间：在 64 位系统上，ob_refcnt 占用 8 字节（Py_ssize_t）。

不可见性：在 Python 层面你无法直接通过属性访问它，通常需要使用 sys.getrefcount()。

2. 堆内存布局图解
当你创建一个对象（例如 a = 1000）时，Python 会在堆（Heap）上分配一块连续的空间。

PyObject_HEAD (头部)：

ob_refcnt：引用计数器。只要有一个变量指向它，计数加 1；变量销毁或指向别处，计数减 1。

ob_type：指向类型对象（Type Object），告诉 Python 这是一个整数、字符串还是自定义类。

Object Body (主体)：

存储对象的实际数据（例如整数的值 1000，或者列表的指针数

3. 特殊情况：GC 头部（PyGC_Head）
如果你提到的“变相”是指为了处理循环引用而存在的结构，那么在支持垃圾回收（GC）的对象（如 list, dict, tuple 以及自定义类实例）中，在 PyObject 的前面还有一部分内存：

PyGC_Head：这部分内存用于将所有“容器对象”串联成双向链表，方便垃圾回收器进行“标记-清除”。

虽然 PyGC_Head 参与了垃圾回收，但核心的引用计数依然雷打不动地放在 PyObject 的 ob_refcnt 里。

"""
# 如何验证？
# 你可以使用 sys 模块直接从堆内存中读取这个数值：
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 通常输出 2（变量 x 引用一次，函数参数临时引用一次）

y = x
print(sys.getrefcount(x))  # 输出 3

# 总结： 引用计数就存在于堆内存中每一个对象实例最头部的 ob_refcnt 字段中。它是 Python 内存管理的第一道防线