import sys
from pathlib import Path
import unittest

current_file_path = Path(__file__).resolve()
parent_path = current_file_path.parent.parent
sys.path.append(str(parent_path))

from BST import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_predecessor(self):
        keys = [50, 30, 70, 20, 40, 60, 80]
        tree = BinarySearchTree()
        [tree.insert(key) for key in keys]
        self.assertEqual(tree.get_predecessor(70), 60)

        keys = [50, 30, 70, 20, 40]
        tree = BinarySearchTree()
        [tree.insert(key) for key in keys]
        self.assertEqual(tree.get_predecessor(30), 20)

        keys = [50, 30, 70, 20, 40, 60, 80]
        tree = BinarySearchTree()
        [tree.insert(key) for key in keys]
        self.assertEqual(tree.get_predecessor(20), 30)



if __name__ == "__main__":
    unittest.main()