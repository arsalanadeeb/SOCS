#linking
from Node import Node

class LinkedList:
    def __init__(self,starter=[]):
        self.head = None
        if len(starter)>0:
            self.head = Node(starter[0])
            current = self.head
            for item in starter[1:]:
               current.next =  Node(item)
               current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  

ll = LinkedList([1, 2, 3, 4, 5])
ll.print_list()     




    