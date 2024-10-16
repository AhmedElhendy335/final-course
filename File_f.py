# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def print_list(self):
#         item = self.head
#         list_item = []
#         while item :
#             list_item.append(item.data)
#             item = item.next
#         return list_item
    
    
        
# list = LinkedList()
# first = Node(1)
# second = Node(2)
# third = Node(3)

# list.head = first
# first.next = second
# second.next = third

# print(list.print_list())






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
        while item :
            list_item.append(item.data)
            item = item.next
        return list_item
    
    def push(self, new_node):
        new_node = Node(new_node)            
        new_node.next = self.head
        self.head = new_node


    def insert(self, new_node, prev_node):
        if prev_node is None:
            raise ValueError
        new_node = Node(new_node)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next :
            last = last.next
        last.next = new_node
        
        
list = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)

list.head = first
first.next = second
second.next = third
list.push(0)
list.insert(second, 9)
print(list.print_list())