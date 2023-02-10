"""Singly  Linked List"""
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        if self.head == None:
            print("List is empty")
        else:
            pos = self.head
            while pos!= None:
                print("->", pos.name, end=" ")
                pos = pos.next
            print()
        return
    def insertFront(self, data):
        pNew = DataNode(data)
        if  self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
    def insertLast(self, data):
        pos = self.head
        while pos.next != None:
            pos = pos.next
        pNew = DataNode(data)
        pos.next = pNew
        self.count += 1
    def insertBefore(self, node, data):
        pNew = DataNode(data)
        if self.head == None:
            return print("Connot Insert, <%s> dose not exist" %data)
        if self.head.name == node:
            pNew.next = self.head
            self.head = pNew
            self.count += 1
            return
        pos = self.head
        while pos.next != None:
            if pos.next.name == node:
                pNew.next = pos.next
                pos.next = pNew
                self.count += 1
                return
            pos = pos.next
        return print("Connot Insert, <%s> dose not exist" %data)
    def delete(self, data):
        if self.head == None:
            return print("Connot Delete, <%s> dose not exist" %data)
        if self.head.name == data:
            delete_data = self.head
            self.head = self.head.next
            delete_data = None
            self.count -= 1
            return
        pos = self.head
        while pos.next != None:
            if pos.next.name == data:
                delete_data = pos.next
                pos.next = pos.next.next
                delete_data = None
                self.count -= 1
                return
            pos = pos.next
        return print("Connot Delete, <%s> dose not exist" %data)

class DataNode:
    def __init__(self, input_name):
        """Create a DataNode"""
        self.name = input_name
        self.next = None

list1 = SinglyLinkedList()
list1.insertFront("Dog")
list1.insertLast("Ant")
list1.insertBefore("Dog", "Bird")
list1.delete("Bird")
list1.traverse()