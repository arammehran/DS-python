class BSTNode:
    def __init__(self, new_val=None):
        self.left = None
        self.right = None
        self.new_val = new_val

    def insert(self, new_val):
        if not self.new_val:
            self.new_val = new_val
            return

        if self.new_val == new_val:
            return

        if new_val < self.new_val:
            if self.left:
                self.left.insert(new_val)
                return
            self.left = BSTNode(new_val)
            return

        if self.right:
            self.right.insert(new_val)
            return
        self.right = BSTNode(new_val)

    def search(self, find_val):
        if find_val == self.new_val:
            return True

        if find_val < self.new_val:
            if self.left == None:
                return False
            return self.left.search(find_val)

        if self.right == None:
            return False
        return self.right.search(find_val)
    
# Set up tree
tree = BSTNode(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
