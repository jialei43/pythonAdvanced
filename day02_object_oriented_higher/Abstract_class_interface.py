"""
抽象类：
"""


class AC(object):
    def make_cool(self):
        """
        制冷
        :return:
        """

        pass

    def make_hot(self):
        """
        制热
        """
        pass

    def make_wide(self):
        """
        摆风
        """
        pass


class Media(AC):
    def make_cool(self):
        print('美的制冷')

    def make_hot(self):
        print('美的制热')

    def make_wide(self):
        print('美的摆风')


class Gree(AC):
    def make_cool(self):
        print('格力制冷')

    def make_hot(self):
        print('格力制热')

    def make_wide(self):
        print('格力摆风')


def pingtai(ac: AC):
    ac.make_cool()
    ac.make_hot()
    ac.make_wide()


media = Media()
gree = Gree()
pingtai(media)
pingtai(gree)
