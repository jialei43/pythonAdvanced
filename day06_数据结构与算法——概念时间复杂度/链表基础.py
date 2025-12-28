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
        # 维护尾部指针
        self.tail = None


    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def getListLength(self):
        length = 0
        if self.isEmpty():
            return 0
        cur = self.head
        while cur != None:
            length += 1
            cur = cur.next
        return length

    def append(self, *args,flag=1)->None:
        '''
        通用链表插入，支持从头部和尾部进行插入，支持单个元素及可迭代容器批量插入
        :param args:
        :param flag: 0-头部 1-尾部 默认是1-尾部
        :return:
        '''
        for item in args:
            if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                for data in item:
                    if flag ==1:
                        self._append_one(data)
                    elif flag ==0:
                        self._add_head_one(data)


            else:
                if flag == 1:
                    self._append_one(item)
                elif flag == 0:
                    self._add_head_one(item)

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
                self.tail=last_item
            self.tail.next = node
            self.tail = node

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

    def add_item_to_head(self,*args):
        for arg in args[0]:
            new_node =SingleNode(arg)
            if self.isEmpty():
                self.head = new_node
            else:
                # 获取当前head的节点
                cur = self.head
                # 将head的新节点设置为新节点
                self.head = new_node
                # 新节点的next节点指向以前的head节点
                new_node.next = cur
        print('所有元素添加完毕')

    # 在指定节点进行数据插入
    def universal_insert_by_index(self,*args,pos):
        '''

        :param args:
        :param pos:
        :return:
        '''
        for item in args:
            if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                for data in item:
                    self._insert_one_by_index(data,pos)
            else:
                self._insert_one_by_index(data,pos)
    def _insert_one_by_index(self,data):
        length = self.getListLength()
        # if

    def getlist(self):
        if not self.isEmpty():
            cur = self.head
            while cur != None:
                print(cur.item)
                cur=cur.next



if __name__ == '__main__':
    single_list = singlelinklist()
    list = [e for e in range(100)]
    # single_list.add_item_to_head(list)
    single_list.append(list,flag=0)
    # single_list.getlist()
    print('==' * 34)
    single_list.append([e for e in range(100,200)],[e for e in range(200,300)])
    single_list.append(300)
    single_list.getlist()
    print('==' * 34)
    is_empty = single_list.isEmpty()
    print(is_empty)
    len = single_list.getListLength()
    print(len)
    # single_list.getlist()
