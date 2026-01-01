from typing import Iterable


class SingleNode(object):

    def __init__(self, data):
        '''

        :param date:传入的数据，存储在元素域
        self.next:连接域存储下个节点的内存地址（也就是对象）
        '''
        self.item = data
        self.next = None


class singlelinklist():

    def __init__(self, node=None):
        self.head = node
        # 维护尾部元素，便于尾部插入时使用，不用遍历获取尾部元素进行插入，提升性能
        self.tail = None
        # 当前索引要插入位置对应的元素
        self.pos_item = None
        # 当前索引要插入位置前一个节点对应的元素
        self.previous_pos_item = None
        # 列表长度
        self.length = 0

    def isEmpty(self):
        '''
        判断是否为空
        :return: bool
        '''
        if self.head == None:
            return True
        else:
            return False

    def getListLength(self):
        """
        获取列表的长度
        :return: int
        """
        length = 0
        if self.isEmpty():
            return 0
        cur = self.head
        while cur != None:
            length += 1
            cur = cur.next
        return length

    def append(self, *args, flag=1, pos=1) -> None:
        '''
        通用链表插入，支持从头部和尾部及指定位置进行插入，支持单个元素及可迭代容器批量插入
        :param args:
        :param flag: 0-头部 1-尾部 2-指定位置进行插入  默认是1-尾部
        :param pos 指定的位置 pos = 1 默认是尾部
        :return:
        '''
        # 若插入的是容易，那么pos没插入一条数据，就需要自增一
        index = pos
        for item in args:
            if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                for data in item:
                    if flag == 1:
                        self._append_one(data)
                    elif flag == 0:
                        self._add_head_one(data)
                    elif flag == 2:
                        self._insert_one_by_index(data, index)
                        index += 1


            else:
                if flag == 1:
                    self._append_one(item)
                elif flag == 0:
                    self._add_head_one(item)
                elif flag == 2:
                    self._insert_one_by_index(item, pos)
        # 循环结束后，清空self.pos_item，elf.previous_pos_item
        # 当前索引要插入位置对应的元素
        self.pos_item = None
        # 当前索引要插入位置建一个节点对应的元素
        self.previous_pos_item = None

    def _append_one(self, data):
        node = SingleNode(data)

        if self.head is None:
            self.head = self.tail = node
        else:
            if self.tail is None:
                cur = self.head
                # 存储最后一个元素
                last_item = None
                while cur != None:
                    last_item = cur
                    cur = cur.next
                self.tail = last_item
            self.tail.next = node
            self.tail = node
        self.length += 1

    def _add_head_one(self, data):
        new_node = SingleNode(data)
        if self.isEmpty():
            self.head = new_node
        else:
            # 获取当前head的节点
            cur = self.head
            # 将head的新节点设置为新节点
            self.head = new_node
            # 新节点的next节点指向以前的head节点
            new_node.next = cur
        self.length += 1

    # def add_item_to_head(self, *args):
    #     for arg in args[0]:
    #         new_node = SingleNode(arg)
    #         if self.isEmpty():
    #             self.head = new_node
    #         else:
    #             # 获取当前head的节点
    #             cur = self.head
    #             # 将head的新节点设置为新节点
    #             self.head = new_node
    #             # 新节点的next节点指向以前的head节点
    #             new_node.next = cur
    #     print('所有元素添加完毕')

    def _insert_one_by_index(self, data, pos):
        length = self.getListLength()
        # 记录当前元素的索引
        index = 0
        node = SingleNode(data)
        if pos <= 0:
            self._add_head_one(data)
        if pos >= length:
            self._append_one(data)
        else:
            if self.pos_item is not None and self.previous_pos_item is not None:
                self.previous_pos_item.next = node
                node.next = self.pos_item
                # 插入完成后更新前一个节点和当前节点
                self.previous_pos_item = node
                # 由于每次插入一个元素，这个元素后面的元素都会往后位移一位，索引当前索引的元素一直不变就不再赋值了
                # self.pos_item = cur

            else:
                cur = self.head
                self.previous_pos_item = None
                while cur is not None:
                    if cur.next is not None:
                        self.previous_pos_item = cur
                        cur = cur.next
                        index += 1
                    if index == pos:
                        break
                self.previous_pos_item.next = node
                node.next = cur
                # 插入完成后更新前一个节点和当前节点
                self.previous_pos_item = node
                self.pos_item = cur

    def getlist(self):
        if not self.isEmpty():
            cur = self.head
            while cur != None:
                print(cur.item)
                cur = cur.next

    #   按照指定的数据进行删除
    def del_by_data(self, *args):
        for arg in args:
            if isinstance(arg, Iterable) and not isinstance(arg, (str, bytes)):
                for data in arg:
                    self.del_one_by_data(data)
            else:
                self.del_one_by_data(arg)

    def del_one_by_data(self, data):
        # 当前节点
        cur = self.head
        # 前一个节点
        pre = None
        count = 0
        while cur is not None:
            if cur.item == data:
                if pre is None:
                    self.head = cur.next
                    if self.length == 1:
                        self.tail = None
                    self.length -= 1
                    # 因为我这个是列表，删除一个之后不可以退出方法
                    # return
                else:
                    # 将前一个节点的next指向 cur的下一个节点，当前节点cur就从列表中删除
                    pre.next = cur.next
                    # 如果删除的节点是最后一个节点
                    if cur.next is  None:
                        self.tail = pre
                    elif self.length == 1:
                        self.tail = None
                    self.length -= 1
                    # 因为我这个是列表，删除一个之后不可以退出方法
                    # return
            # 走入这个逻辑，说明没找到要删除的节点，那么需要将当前的节点更新为前一个节点，将下一个节点更新为当前节点
            pre = cur
            cur = cur.next


    '''
    查找和遍历类似，只需按照链表next指针访问，直到找到匹配的数据节点
    '''

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.item == data:
                return True
            # 没找到则更新cur节点为下一个节点
            cur = cur.next
        return False


if __name__ == '__main__':
    single_list = singlelinklist()
    my_list = [e for e in range(100)]
    # single_list.add_item_to_head(list)
    single_list.append(my_list, flag=0)
    # single_list.getlist()
    print('==' * 34)
    single_list.append([e for e in range(100, 200)], [e for e in range(200, 300)])
    single_list.append(300)
    # single_list.getlist()
    print('==' * 34)
    single_list.append([e for e in range(500, 600)], [e for e in range(600, 700)], flag=2, pos=100)
    single_list.append(701, flag=2, pos=100)
    # single_list.getlist()
    print('==' * 34)
    # 删除指定的数据
    single_list.del_by_data([99, 701, 500, 501, 502, 503, 504, 505, 506, 507])
    single_list.del_by_data(508)
    single_list.getlist()
    print('==' * 34)
    print(single_list.search(508))
    print(single_list.search(509))
    print('==' * 34)
    is_empty = single_list.isEmpty()
    print(is_empty)
    len = single_list.getListLength()
    print(len)
    # single_list.getlist()
