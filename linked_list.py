#!/usr/bin/env python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def initlist(self,data_list):
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def is_empty(self):
        if self.head == None:
            print("Linked_list is empty")
            return True
        else:
            return False

    def get_length(self):
        temp = self.head
        length = 0
        while temp != None:
            length = length + 1
            temp = temp.next
        return length

    def insert(self,key,value):
        if key <0 or key >self.get_length() - 1:
            print("insert error")
        temp = self.head
        i = 0
        while i <= key:
            pre = temp
            temp = temp.next
            i = i + 1
        node = Node(value)
        pre.next = node
        node.next = temp

    def print_list(self):
        print("linked_list")
        temp =self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def remove(self,key):
        if key <0 or key >self.get_length() -1:
            print("insert error")
        i=0
        temp = self.head
        while temp != None:
            pre = temp
            temp = temp.next
            i = i+1
            if i == key:
                pre.next = temp.next
                temp = None
                return True
        pre.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
        self.head = prev

    def swapNode(self,d1,d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 =D1
                D1 = D1.next
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            if D1 is None and D2 is None:
                return
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

    def add_fronted(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    list = Linked_List()
    list.add_fronted(5)
    list.add_fronted(4)
    list.add_fronted(3)
    list.add_fronted(2)
    list.add_fronted(1)
    list.print_list()
    list.swapNode(1,4)
    print("after swapping")
    list.print_list()






