class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __int__(self):
        self.head = None

    def print_list(self):
        item = self.head
        while item:
            #list_item.append(item.data)
            print(item.data)
            item = item.next


llist = linkedlist()

first = Node(1)
second = Node(2)
third = Node(3)

llist.head = first
llist.head.next = second
second.next = third


#llist.print_list()
print(list.print_list())