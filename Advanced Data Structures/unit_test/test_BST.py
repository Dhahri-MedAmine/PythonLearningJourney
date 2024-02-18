from ast import List
import sys
from pathlib import Path
import unittest

current_file_path = Path(__file__).resolve()
parent_path = current_file_path.parent.parent
sys.path.append(str(parent_path))

from BST import BinarySearchTree

def getTree(keys) -> BinarySearchTree:
    tree: BinarySearchTree = BinarySearchTree()
    [tree.insert(key) for key in keys]
    return tree


class TestBinarySearchTree(unittest.TestCase):
    def test_predecessor(self):
        tree = getTree([50, 30, 70, 20, 40, 60, 80])
        self.assertEqual(tree.get_predecessor(70), 60)
        self.assertEqual(tree.get_predecessor(20), None)
        self.assertEqual(tree.get_predecessor(11), None)

        tree = getTree([50, 30, 70, 20, 40])
        self.assertEqual(tree.get_predecessor(30), 20)

        tree = BinarySearchTree()
        self.assertEqual(tree.get_predecessor(30), None)

    def test_successor(self):
        tree = getTree([50, 30, 70, 20, 40, 60, 80])
        self.assertEqual(tree.get_successor(50), 60)  # Successor of root node
        self.assertEqual(tree.get_successor(40), 50)  # Successor of a node with right child
        self.assertEqual(tree.get_successor(80), None)  # Successor of max node

        tree = getTree([50, 30, 70, 20, 40])
        self.assertEqual(tree.get_successor(20), 30)  # Successor of a leaf node

        tree = getTree([])
        self.assertEqual(tree.get_successor(30), None)  # Empty tree

        tree = getTree([50])
        self.assertEqual(tree.get_successor(50), None)  # Single node tree

        tree = getTree([50, 30])
        self.assertEqual(tree.get_successor(30), 50)  # Successor in a tree with only left child

        tree = getTree([50, 70])
        self.assertEqual(tree.get_successor(50), 70)  # Successor in a tree with only right child




if __name__ == "__main__":
    unittest.main()