# 步骤 1: 创建日志记录基类
#
# 我们首先定义一个日志记录的基类，所有的日志记录器都需要继承它。
class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses must implement this method.")

# 步骤 2: 定义不同的日志记录方式
#
# 我们可以为不同的日志记录方式（如文件日志、控制台日志等）提供具体的实现。
class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(f"[File Log] {message}\n")


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console Log] {message}")


class RemoteLogger(Logger):
    def log(self, message):
        # 假设这是发送日志到远程服务器的操作
        print(f"[Remote Log] {message} (Sent to remote server)")

# 步骤 3: 定义元类
#
# 元类用于动态创建日志管理器类，并决定日志记录的方式。我们根据不同的环境配置选择不同的日志方式
class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        # 根据环境变量来决定使用哪种日志方式
        import os
        env = os.getenv("APP_ENV", "development")  # 默认使用开发环境

        if env == "production":
            dct['logger'] = FileLogger("app.log")  # 生产环境使用文件日志
        elif env == "development":
            dct['logger'] = ConsoleLogger()  # 开发环境使用控制台日志
        else:
            dct['logger'] = RemoteLogger()  # 其他环境使用远程日志

        return super().__new__(cls, name, bases, dct)

# 步骤 4: 定义日志管理器类
#
# 使用元类 LoggerMeta 来动态创建一个日志管理器类，它会根据环境配置初始化合适的日志记录方式。
class LoggerManager(metaclass=LoggerMeta):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the LoggerManager instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        self.logger.log(message)

# 步骤 5: 测试代码
#
# 我们将模拟不同的环境配置，并使用日志管理器来记录日志。
import os

# 设置环境变量模拟不同的环境
os.environ["APP_ENV"] = "development"  # 可以切换为 "production" 或其他环境

# 创建日志管理器实例
logger_manager1 = LoggerManager()
logger_manager1.log("This is a test log in development environment.")

# 再次创建实例，检查是否是同一个实例
logger_manager2 = LoggerManager()
print(logger_manager1 is logger_manager2)  # 输出: True
'''
关键点解释：

LoggerMeta 元类：

在 LoggerMeta 中，我们通过 __new__ 方法动态决定使用哪种日志记录方式。根据环境变量（APP_ENV），我们选择了不同的日志记录类（文件日志、控制台日志、远程日志）。

单例模式：

在 LoggerManager 类中，我们使用 __new__ 方法确保只有一个日志管理器实例被创建。即使多次创建 LoggerManager 实例，它们都是同一个对象。

日志记录：

LoggerManager 始终持有一个日志记录器对象（self.logger），它根据环境配置选择合适的日志记录方式。

扩展应用：

分布式系统：对于分布式系统，日志管理器可以使用远程日志服务进行日志收集。

日志轮转：对于生产环境，可以扩展文件日志记录类以支持日志轮转，避免日志文件过大。

多环境支持：可以根据不同的环境（如开发、生产、测试等）配置不同的日志级别和记录方式（比如错误级别、调试级别等）。

总结：

通过 元类 和 单例模式，我们实现了一个灵活的日志管理系统，可以根据不同的环境配置不同的日志记录方式，并确保系统中只有一个日志管理器实例。这种设计方式在企业级应用中非常常见，尤其是在需要灵活配置和控制对象创建的场景下
'''
