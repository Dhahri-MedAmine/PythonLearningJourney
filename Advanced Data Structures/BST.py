from random import choice
from BST_Node import Node

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        self.root.insert(data)

    def search(self, data):
        if self.root is None:
            return None

        return self.root.search(data)

    def display(self, order=Node.TRAVERSALS.IN_ORDER):
        if self.root is None:
            print(None)
            return

        self.root.display(order)

    def find_LCA(self, node1, node2):
        if self.root is None:
            return None

        return self.root.find_LCA(node1, node2)

    def get_predecessor(self, key):
        if self.root is None:
            return None
        
        return self.root.get_predecessor(key)
    
    def get_successor(self, key):
        if self.root is None:
            return None
        
        return self.root.get_successor(key)

if __name__ == "__main__":
    BST = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    [BST.insert(key) for key in keys]

    BST.display(Node.TRAVERSALS.IN_ORDER)
    BST.display(Node.TRAVERSALS.PRE_ORDER)
    BST.display(Node.TRAVERSALS.POST_ODER)

    print(BST.get_predecessor(30))


    print(BST.find_LCA(choice(keys), choice(keys)))
