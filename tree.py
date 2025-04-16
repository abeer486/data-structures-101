class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Only numeric values are allowed.")
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def inorder(self, node):
        if self.root is None:
            raise ValueError("The tree is empty.")
        stack, result = [], []
        current = node
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

# Example usage
bt = BinaryTree()
for value in [8, 3, 10, 1, 6, 4, 7, 14, -1, 1.09]:
    bt.insert(value)

print("Inorder traversal of the binary tree:")
print(bt.inorder(bt.root))


# Another example
bt2 = BinaryTree()
for value in [5, 3, 8, 1, 4]:
    bt2.insert(value)  

print("\nInorder traversal of the second binary tree:")
print(bt2.inorder(bt2.root))