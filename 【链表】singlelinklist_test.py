#! usr/bin/env python3
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    # 单向链表的操作
    def travel(self):  # 遍历
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def length(self):  # 长度
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):  # 搜索
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False

    def substance(self, item, newitem):  # 替换
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                cur.elem = newitem
                return
            cur = cur.next
        print("not find")

    # 插入
    def hinsert(self, item):  # 在开始处插入
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):  # 在末尾插入
        node = Node(item)
        cur = self.__head
        if self.__head is None:
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):  # 在任意位置插入
        node = Node(item)
        if pos <= 0:
            self.hinsert(item)
        elif pos >= self.length():
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    # 删除
    def hdelete(self):  # 在开始处删除
        if self.__head is not None:
            self.__head = self.__head.next

    def tdelete(self):  # 在末尾删除
        cur = self.__head
        prev = None
        if self.__head is not None:
            if self.__head.next is not None:
                while cur.next is not None:
                    prev = cur
                    cur = cur.next
                prev.next = None
            else:
                self.__head = None

    # def delete(self, item):  # 删除任意元素





if __name__ == "__main__":
    sll = SingleLinkList()
    print(sll.length())
    sll.append(7)
    sll.hinsert(111)
    sll.hinsert(20)
    sll.hinsert(555)
    sll.append(568)
    sll.travel()
    print(sll.length())
    sll.insert(1, 8888)
    sll.travel()
    sll.insert(-1, 8885)
    sll.travel()
    sll.insert(6, 8888)
    sll.travel()
    sll.insert(9, 8889)
    sll.travel()
    print(sll.search(8889))
    print(sll.search(8885))
    print(sll.search(10086))
    print("*" * 50)
    sll.substance(8888, 9999)
    sll.travel()
    sll.substance(10086, 9999)
    sll.substance(8885, 110)
    sll.travel()
    sll.substance(8889, 1200)
    sll.travel()
    print("*" * 50)

    print("*" * 50)
    sll2=SingleLinkList()
    sll2.hdelete()
    sll2.travel()