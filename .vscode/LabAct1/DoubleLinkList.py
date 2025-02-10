class Node:
    def __init__(self, data=None):
        self.data = data  # Data stored in the node
        self.next = None  # Points to the next node
        self.prev = None  # Points to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the linked list is empty

    # Method to append a node to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            cur = self.head
            while cur.next:  # Traverse to the last node
                cur = cur.next
            cur.next = new_node  # Link the last node to the new node
            new_node.prev = cur  # Set the previous pointer of the new node to the last node

    # Method to print the list from head to tail
    def display_forward(self):
        cur = self.head
        while cur:  # Traverse the list from head to tail
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")

    # Method to print the list from tail to head
    def display_backward(self):
        cur = self.head
        while cur and cur.next:  # Traverse to the last node
            cur = cur.next
        while cur:  # Traverse backwards
            print(cur.data, end=" <-> ")
            cur = cur.prev
        print("None")

    # Method to get the length of the list
    def length(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total

    # Method to get the data of a node by index
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.data

    # Method to delete a node by value
    def delete(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:  # If the node is not the first node
                    cur.prev.next = cur.next
                if cur.next:  # If the node is not the last node
                    cur.next.prev = cur.prev
                if cur == self.head:  # If the node is the head
                    self.head = cur.next
                cur = None  # Delete the node
                print(f"Deleted: {data}")
                return
            cur = cur.next
        print(f"Node with data {data} not found.")

# Example usage:
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Display Forward:")
dll.display_forward()  # Output: 10 <-> 20 <-> 30 <-> 40 <-> None

print("\nDisplay Backward:")
dll.display_backward()  # Output: 40 <-> 30 <-> 20 <-> 10 <-> None

# Get element at a specific index
print("\nGet element at index 2:")
print(dll.get(2))  # Output: 30

# Delete a node by value
print("\nDelete node with value 30:")
dll.delete(30)
dll.display_forward()  # Output: 10 <-> 20 <-> 40 <-> None
