from typing import Optional


class BinaryTree:

    def __init__(self, key):
        self._key: str = str(key)
        self._left_child: Optional[BinaryTree] = None
        self._right_child: Optional[BinaryTree] = None

    def get_root_key(self) -> str:
        return self._key

    def set_root_key(self, new_key: str) -> None:
        self._key = new_key

    def get_left_child(self) -> "Optional[BinaryTree]":
        return self._left_child

    def get_right_child(self) -> "Optional[BinaryTree]":
        return self._right_child

    def insert_left(self, value):
        if self._left_child is None:
            self._left_child = BinaryTree(value)
        else:
            new_tree = BinaryTree(value)
            new_tree._left_child = self._left_child
            self._left_child = new_tree

    def insert_right(self, value):
        if self._right_child is None:
            self._right_child = BinaryTree(value)
        else:
            new_tree = BinaryTree(value)
            new_tree._right_child = self._right_child
            self._right_child = new_tree

    def preorder(self):
        print(self._key, end=' -> ')
        if self._left_child:
            self._left_child.preorder()
        if self._right_child:
            self._right_child.preorder()

    def add_left_subtree(self, new_tree):
        if self.get_left_child() is None:
            self._left_child = new_tree
        else:
            old_child = self._left_child
            self._left_child = new_tree
            last_left_child = self._left_child
            while last_left_child.get_left_child() is not None:
                last_left_child = last_left_child.get_left_child()
            last_left_child._left_child = old_child

    def add_right_subtree(self, new_tree):
        if self.get_right_child() is None:
            self._right_child = new_tree
        else:
            old_child = self._right_child
            self._right_child = new_tree
            last_right_child = self._right_child
            while last_right_child.get_right_child() is not None:
                last_right_child = last_right_child.get_right_child()
            last_right_child._right_child = old_child


