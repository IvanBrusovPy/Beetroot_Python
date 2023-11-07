from copy import deepcopy

from tree import BinaryTree



if __name__ == '__main__':
    base_tree = BinaryTree(1)
    base_tree.insert_left(6)
    base_tree.insert_left(4)
    base_tree.insert_left(2)
    base_tree.get_left_child().insert_right(5)
    base_tree.insert_right(7)
    base_tree.insert_right(3)

    sub_tree = BinaryTree(6)
    sub_tree.insert_left(10)
    sub_tree.insert_right(4)
    base_tree.add_left_subtree(deepcopy(sub_tree))
