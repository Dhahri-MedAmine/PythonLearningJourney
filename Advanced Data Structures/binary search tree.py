from typing import Optional
from enum import Enum
from random import choice


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    class TRAVERSALS(Enum):
        IN_ORDER = 1
        PRE_ORDER = 2
        POST_ODER = 3

    @staticmethod
    def __insert_node(node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = Node.__insert_node(node.left, data)
        if data > node.data:
            node.right = Node.__insert_node(node.right, data)

        return node

    def insert(self, data):
        Node.__insert_node(self, data)

    @staticmethod
    def __display_node(node, order=TRAVERSALS.IN_ORDER):
        if node is None:
            return

        if order == Node.TRAVERSALS.IN_ORDER:
            Node.__display_node(node.left, order)
            print(node.data, end=" ")
            Node.__display_node(node.right, order)

        if order == Node.TRAVERSALS.PRE_ORDER:
            print(node.data, end=" ")
            Node.__display_node(node.left, order)
            Node.__display_node(node.right, order)

        if order == Node.TRAVERSALS.POST_ODER:
            Node.__display_node(node.left, order)
            Node.__display_node(node.right, order)
            print(node.data, end=" ")

    def display(self, order=TRAVERSALS.IN_ORDER):
        Node.__display_node(self, order)
        print()

    @staticmethod
    def __search_node(node, data):
        if data == node.data:
            return node

        if data < node.data and node.left is not None:
            return Node.__search_node(node.left, data)

        if data > node.data and node.right is not None:
            return Node.__search_node(node.right, data)

        return None

    def search(self, data):
        return Node.__search_node(self, data)

    @staticmethod
    def __find_LCA(root, data1, data2):
        if (
            (data1 < root.data < data2)
            or (data1 > root.data > data2)
            or data1 == root.data
            or data2 == root.data
        ):
            return root

        if (data1 < root.data) and (data2 < root.data):
            return Node.__find_LCA(root.left, data1, data2)

        if (data1 > root.data) and (data2 > root.data):
            return Node.__find_LCA(root.right, data1, data2)

    def find_LCA(self, data1, data2):
        if self.search(data1) is None or self.search(data2) is None:
            return None

        return Node.__find_LCA(self, data1, data2)

    def __str__(self) -> str:
        return f"{self.data}"


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

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



if __name__ == "__main__":
    BST = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    [BST.insert(key) for key in keys]

    BST.display(Node.TRAVERSALS.IN_ORDER)
    BST.display(Node.TRAVERSALS.PRE_ORDER)
    BST.display(Node.TRAVERSALS.POST_ODER)

    print(BST.find_LCA(choice(keys), choice(keys)))
