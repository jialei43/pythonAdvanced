"""
烤地瓜案例
需求：
    属性：
        地瓜状态
        调料列表
        考的时间
    行为：
        烤地瓜
        添加调料

"""


class BakedSweetPotato:
    def __init__(self):
        self.cook_state = '生的'
        self.condiments = []
        self.cook_time = 0

    def add_condiment(self, condiment):
        if isinstance(condiment,list):
            self.condiments.extend(condiment)
        else:
            self.condiments.append(condiment)


    def cook(self, cook_time):
        if cook_time < 0:
            return
        # 记录烤的时间
        self.cook_time += cook_time
        if self.cook_time > 0 and cook_time <= 3:
            self.cook_state = '生的'
            return
        if 3 < self.cook_time <= 7:
            self.cook_state = '半生不熟'
            return
        if 7 < self.cook_time <= 12:
            self.cook_state = '熟了'
            return
        else:
            self.cook_state = '糊了'
            return

    def __str__(self):
        return (f'地瓜烤了{self.cook_time}分钟,地瓜状态是{self.cook_state},添加调料：{self.condiments}')


if __name__ == '__main__':
    baked_sweet = BakedSweetPotato()
    baked_sweet.add_condiment(['花椒', '大料'])
    # baked_sweet.add_condiment('花椒, 大料')
    baked_sweet.cook(6)
    print(baked_sweet)
    baked_sweet.cook(6)
    print(baked_sweet)
