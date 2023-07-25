class SearchNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left, self.right = l, r

class Tree:
    def __init__(self):
        self.root = None
    def find(self,key):
        return findNode(self.root, key)
    def add(self,key):
        self.root = addNode(self.root, key)