import threading

"""
🔥 为什么这是“最权威”的？
1️⃣ 符合 Python 对象模型
__new__：控制对象创建
__init__：对象初始化
单例的本质是：控制“只能创建一个对象”
所以逻辑必须写在 __new__，不是 __init__
👉 这是 Python 设计哲学层面的正确位置
"""
class Singleton:
    _instance = None
    # 为了实现线程安全还引入了锁机制
    _lock = threading.Lock()
    _initialized = False
    """
    如果不对__init__方法做控制，只有__new__会实现单例，但是会出现下面的问题
    ⚠️ 一个必须补充的现实问题：__init__ 会被多次调用
    """
    def __new__(cls, *args, **kwargs):
        # 第一次检查（无锁，提高性能）
        if cls._instance is None:
            with cls._lock:
                # 第二次检查（防止多线程同时进入）
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=100):
        # 保证 __init__ 只执行一次
        if self._initialized:
            return

        # ===== 真正的初始化逻辑 =====
        self.value = value
        # ===========================

        self._initialized = True
