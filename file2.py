class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        item = self.head
        list_item = []
        while item:
            list_item.append(item.data)
            item = item.next
        return list_item


list = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)

list.head = first
first.next = second
second.next = third

print(list.print_list())