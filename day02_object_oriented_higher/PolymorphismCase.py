"""
多态战斗机演示：
"""
# 基类，所有战斗机的基类
class HeroFlghter(object):
    def __pow__(self):
        return 60

class AdvHeroflghter(HeroFlghter):
    def __pow__(self):
        return 200

class EggHeroflghter(object):
    def __pow__(self):
        return 100

#   搭建一个平台(框架)，让对象唱戏
def object_play(heroflghter: HeroFlghter, eggheroflghter: EggHeroflghter):
    if heroflghter.__pow__() > eggheroflghter.__pow__():
        print("英雄战机胜利，敌机失败")
    else:
        print("英雄战机失败，敌机胜利")

if __name__ == '__main__':
    heroflghter = HeroFlghter()
    eggheroflghter = EggHeroflghter()
    advheroflghter = AdvHeroflghter()
    object_play(heroflghter,eggheroflghter)
    object_play(advheroflghter,eggheroflghter)
