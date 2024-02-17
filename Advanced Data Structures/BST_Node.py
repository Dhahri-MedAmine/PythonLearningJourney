from enum import Enum


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

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

    @staticmethod
    def __get_right_most(node):
        if node is None:
            return None
        if node.right is None:
            return node.data
        else:
            return Node.__get_right_most(node.right)
        
    def get_right_most(self):
        return Node.__get_right_most(self)

    @staticmethod
    def __get_predecessor(node, key):
        if node is None:
            return None

        if key == node.data:
            if node.left is not None:
                return node.left.get_right_most()

        if key < node.data:
            newVal = Node.__get_predecessor(node.left, key)
            if newVal is None or newVal == node.left.data:
                return node.data
            else:
                return newVal

        if key > node.data:
            newVal = Node.__get_predecessor(node.right, key)
            if newVal is None or newVal == node.right.data:
                return node.data
            else:
                return newVal

    def get_predecessor(self, key):
        return Node.__get_predecessor(self, key)

    def __str__(self) -> str:
        return f"{self.data}"
