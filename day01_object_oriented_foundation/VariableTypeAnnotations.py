"""
变量类型注解：
    作用：方便第三方工具进行代码类型推断，协助代码提示和开发者根据函数的类型进行提示
    注解不影响程序执行，即使注解标错，程序依然可以运行
"""
# 变量注解方式一： 变量名称: 类型
var_1: int = 10
var_2: float =3.1414926
var_3: bool = True
var_4: str = 'itheima'

# 方式二：通过注解的方式
var_5 = 10  # int
var_6 =3.1414926 # float
var_7 = True # bool
var_8 = 'itheima' # str

# 基础数据容器注解 也支持注解的方式，为了方便后面都使用注解方式一
my_list:list = [1,2,3,4,5]
my_tuple:tuple = (1,2,3,4,5)
my_set:set = {1,2,3,4,5}
my_dict:dict = {'name':'张三'}

# 复杂容器注解，对容器中的所有元素做注解
my_list:list[int] = [1,2,3,4,5]
my_tuple:tuple[int,int,int,str,bool] = (1,2,3,'itheima',True)
my_set:set[int] = {1,2,3,4,5}
my_dict:dict[str,str] = {'name':'张三'}

