class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

def search(target, node):
    # Node doesn't exist or we found the target
    if node is None or node.value == target:
        return node

    elif target < node.value:
        return search(target, node.leftChild)

    else:
        return search(target, node.rightChild)

def insert(value, node):
    if value < node.value:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)

    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)

def delete(value, node):
    if node is None: return None

    elif value < node.value:
        node.leftChild = delete(value, node.leftChild)
        return node

    elif value > node.value:
        node.rightChild = delete(value, node.rightChild)
        return node
    
    elif value == node.value:
        if node.leftChild is None: return node.rightChild
        elif node.rightChild is None: return node.leftChild

        # Special case where we're deleting a node with two children
        else:
            node.rightChild = lift(node.rightChild, node)
            return node

def lift(node, node_to_delete):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, node_to_delete)
    else:
        node_to_delete.value = node.value
        return node.rightChild

def traverse_and_print(node):
    if node is None: return
    traverse_and_print(node.leftChild)
    print(node.value)
    traverse_and_print(node.rightChild)

def preorder_traverse_and_print(node):
    if node is None: return
    print(node.value)
    preorder_traverse_and_print(node.leftChild)
    preorder_traverse_and_print(node.rightChild)

def postorder_traverse_and_print(node):
    if node is None: return
    postorder_traverse_and_print(node.leftChild)
    postorder_traverse_and_print(node.rightChild)
    print(node.value)

def max(node):
    if node.rightChild: return max(node.rightChild)
    else: return node.value

# Part 1 -- build a binary search tree
print("=== Inserting nodes into a tree...")
root = TreeNode("Moby Dick")
insert("Great Expectations", root)
insert("Robinson Crusoe", root)
insert("Alice in Wonderland", root)
insert("Lord of the Flies", root)
insert("Pride and Prejudice", root)
insert("The Odyssey", root)
print("=== In-order traversal...")
traverse_and_print(root)
print("=== Pre-order traversal...")
preorder_traverse_and_print(root)
print("=== Post-order traversal...")
postorder_traverse_and_print(root)

# Part 2 -- searching a binary search tree
print("=== Find 'The Odyssey'...")
print(search("The Odyssey", root).value)
print("=== Find a title that doesn't exist...")
print(search("No Title", root))

# Part 3 -- delete left child
print("=== Delete left child...")
delete("Pride and Prejudice", root)
traverse_and_print(root)
print("=== Delete right child...")
delete("The Odyssey", root)
traverse_and_print(root)
print("=== Delete the root...")
delete("Moby Dick", root)
traverse_and_print(root)

# Part 4 -- max
print("=== Max value...")
print(max(root))