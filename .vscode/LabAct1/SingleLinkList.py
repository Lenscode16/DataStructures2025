class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()  # Initialize the head of the linked list to an empty node

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:  # Traverse the list to find the last node
            cur = cur.next
        cur.next = new_node  # Link the last node to the new node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:  # Traverse the list and count the nodes
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head.next  # Skip the head node which is empty
        while cur_node is not None:  # Traverse the list and collect data
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head.next  # Skip the head node
        while cur_node is not None:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

# Example usage:
my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()  # Output: [1, 2, 3, 4]

# Get element at a specific index
print(my_list.get(2))  # Output: 3
