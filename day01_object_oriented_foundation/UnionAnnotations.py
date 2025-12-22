"""
当我们容器里有很多数据，且数据类型不一致，此时我们去给变量做注解，就不太方便了
此时，应运而生了Union 联合类注解
使用Union[类型,....,类型] 可以定义联合类型注解
"""
from typing import Union

# 例如
my_list:list[Union[str,int]] = [1, 2, 3, 4, 5 ,'itheima']
my_dict: dict[str,Union[str, int]] = {'name':'John', 'age':22}