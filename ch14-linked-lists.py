# The book's examples were in Ruby, so I got some pointers on how to code
# them in Python from https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DoublyLinkedNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class SinglyLinkedList:
    def ___init__(self):
        self.head = None

    def data_at_index(self, index):
        if index < 0: return None

        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

            if current_node == None: return None
        
        return current_node.data

    def index_of(self, data):
        current_node = self.head
        current_index = 0

        # (TIL there's no do-while loop in Python)
        while True:
            # Found what we're looking for
            if current_node.data == data: return current_index

            # Make sure we don't go off the end of the list
            if current_node.next == None: return None

            current_node = current_node.next
            current_index += 1

    def insert_at_index(self, index, data):
        new_node = Node(data)

        # Special case: insertion at the head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Find where to insert the new node
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            if current_node.next == None: return

            current_node = current_node.next
            current_index += 1

        # Link things up
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_index(self, index):
        # Special case: removing the head
        if index == 0:
            self.head = self.head.next
            return

        # Find the node just before where we need to delete
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            if current_node.next == None: return

            current_node = current_node.next
            current_index += 1

        # Unlink
        node_after_deleted_node  = current_node.next.next
        current_node.next = node_after_deleted_node

    def value_at_tail(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        return current_node.data

    def reverse(self):
        prev = None
        curr = self.head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev
    
    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

class DoublyLinkedList:
    def ___init__(self):
        self.head = None
        self.tail = None

    def data_at_index(self, index):
        if index < 0: return None

        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

            if current_node == None: return None
        
        return current_node.data

    def index_of(self, data):
        current_node = self.head
        current_index = 0

        # (TIL there's no do-while loop in Python)
        while True:
            # Found what we're looking for
            if current_node.data == data: return current_index

            # Make sure we don't go off the end of the list
            if current_node.next == None: return None

            current_node = current_node.next
            current_index += 1

    def insert_at_index(self, index, data):
        new_node = DoublyLinkedNode(data)

        # Special case: insertion at the head
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Find where to insert the new node
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            if current_node.next == None: return

            current_node = current_node.next
            current_index += 1

        # Link things up
        new_node.next = current_node.next
        new_node.prev = current_node
        if new_node.next != None: new_node.next.prev = new_node
        current_node.next = new_node

        if new_node.next == None: self.tail = new_node

    def delete_at_index(self, index):
        # Special case: removing the head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        # Find the node just before where we need to delete
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            if current_node.next == None: return

            current_node = current_node.next
            current_index += 1

        node_after_deleted_node  = current_node.next.next

        # Unlink (case = not the end)
        if node_after_deleted_node != None:
            current_node.next = node_after_deleted_node
            node_after_deleted_node.prev = current_node
        # Unlink (case = deleting last node)
        else:
            current_node.next = None
            self.tail = current_node

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def print_reverse(self):
        current_node = self.tail
        while current_node != None:
            print(current_node.data)
            current_node = current_node.prev

# Part 1 -- basic node linking
node1 = Node("once")
node2 = Node("upon")
node3 = Node("a")
node4 = Node("time")

node1.next = node2
node2.next = node3
node3.next = node4
sll = SinglyLinkedList()
sll.head = node1

# Part 2 -- finding data at a given index
print("=== Index 3 has this value...")
print(sll.data_at_index(3))
print("=== Index 234 (too big) has this value...")
print(sll.data_at_index(234))

# Part 3 -- index of a value
print("=== Index of 'upon'")
print(sll.index_of("time"))
print("=== Index of 'nope'")
print(sll.index_of("nope"))

# Part 4 -- insert at index
print("=== Before insertion...")
sll.print()
print("=== Inserting at the front...")
sll.insert_at_index(0, "now")
sll.print()
print("=== Inserting near the end...")
sll.insert_at_index(4, "purple")
sll.print()

# Part 5 -- delete at index
print("=== Before deletion...")
sll.print()
print("=== Deleting 'purple'...")
sll.delete_at_index(4)
sll.print()
print("=== Deleting first node...")
sll.delete_at_index(0)
sll.print()

 # Part 5 -- doubly-linked node linking
dllnode1 = DoublyLinkedNode("once")
dllnode2 = DoublyLinkedNode("upon")
dllnode3 = DoublyLinkedNode("a")
dllnode4 = DoublyLinkedNode("time")

dllnode1.next = dllnode2

dllnode2.prev = dllnode1
dllnode2.next = dllnode3

dllnode3.prev = dllnode2
dllnode3.next = dllnode4

dllnode4.prev = dllnode3
dll = DoublyLinkedList()
dll.head = dllnode1
dll.tail = dllnode4

print("=== DLL front to back")
dll.print()
print("=== DLL back to front")
dll.print_reverse()

# Part 6 -- finding data at a given index
print("=== DLL index 3 has this value...")
print(dll.data_at_index(3))
print("=== DLL index 234 (too big) has this value...")
print(dll.data_at_index(234))

# Part 7 -- index of a value
print("=== DLL index of 'upon'")
print(dll.index_of("time"))
print("=== DLL index of 'nope'")
print(dll.index_of("nope"))

# Part 8 -- DLL insert at index
print("=== DLL before insertion...")
dll.print()
print("=== DLL inserting at the front...")
dll.insert_at_index(0, "now")
dll.print()
print("=== DLL inserting near the end...")
dll.insert_at_index(4, "purple")
dll.print()
print("=== DLL inserting at end...")
dll.insert_at_index(6, "<end>")
dll.print()
print("=== The list backward to double-check...")
dll.print_reverse()

# Part 9 -- delete at index
print("=== Before deletion...")
dll.print()
print("=== Deleting 'purple'...")
dll.delete_at_index(4)
dll.print()
print("=== Deleting first node...")
dll.delete_at_index(0)
dll.print()
print("=== Deleting last node...")
dll.delete_at_index(4)
dll.print()
print("=== The list backward to double-check...")
dll.print_reverse()

# Part 10 -- tail of singly linked list
print("=== Tail of SLL")
print(sll.value_at_tail())

# Part 11 - reverse an SLL
print("=== Before SLL reversal...")
sll.print()
print("=== After SLL reversal...")
sll.reverse()
sll.print()