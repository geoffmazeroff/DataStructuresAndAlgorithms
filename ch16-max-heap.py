class Heap:
    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[len(self.data)-1]

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        # New data always goes at the end of the array
        self.data.append(value)

        new_node_index = len(self.data) - 1
        new_node_index_is_not_the_root = new_node_index > 0
        parent_is_less_than_new_node = self.data[new_node_index] > self.data[self.parent_index(new_node_index)]

        while new_node_index_is_not_the_root and parent_is_less_than_new_node:
            
            # Swap the new node with the parent
            new_node_parent_index = self.parent_index(new_node_index)
            self.data[new_node_parent_index], self.data[new_node_index] = self.data[new_node_index], self.data[new_node_parent_index]

            # We've moved up toward the top of the heap
            new_node_index = new_node_parent_index

            # Update conditions for the while-loop
            new_node_index_is_not_the_root = new_node_index > 0
            parent_is_less_than_new_node = self.data[new_node_index] > self.data[self.parent_index(new_node_index)]

    def has_greater_child(self, index):
        # Check if the node at the given index has left and right children,
        # and if either of those children are greater than the node at the given index.
        data_at_index = self.data[index]
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        if left_child_index < len(self.data):
            return self.data[left_child_index] > data_at_index
        if right_child_index < len(self.data):
            return self.data[right_child_index] > data_at_index
        
        # No children
        return False

    def calculate_greater_child(self, index):
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        # If there's only one child, the non-missing one is the greater child
        # Note: because of the heap structure, it's impossible to have a right
        # child with no left child.
        if right_child_index >= len(self.data):
            return left_child_index
        
        # Left < right
        if self.data[left_child_index] < self.data[right_child_index]:
            return right_child_index
        
        # Left >= right
        return left_child_index

    def delete(self):
        if len(self.data) == 0: return

        # Only the root node gets replaced with the last node
        self.data[0] = self.data.pop()
        trickle_node_index = 0

        # Heapify the structure now that the root has changed
        while self.has_greater_child(trickle_node_index):
            greater_child_index = self.calculate_greater_child(trickle_node_index)

            # Swap trickle node with bigger child
            self.data[trickle_node_index], self.data[greater_child_index] = self.data[greater_child_index], self.data[trickle_node_index]

            trickle_node_index = greater_child_index

# Part 1 -- construct a heap
heap = Heap()
for x in range(1,11): heap.insert(x)
print("=== In a heap with numbers 1 through 10...")
print("=== First node is...")
print(heap.root_node())
print("=== Last node is...")
print(heap.last_node())

# Part 2 -- remove the root
print("=== Removing the root...")
heap.delete()
print("=== First node is...")
print(heap.root_node())
print("=== Last node is...")
print(heap.last_node())