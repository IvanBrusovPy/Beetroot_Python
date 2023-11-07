from graph import Tree

if __name__ == '__main__':
    test_tree = Tree()

    file_path = "test_task2.html"
    test_tree.parseHTML(file_path)
    print(test_tree.print_tree())
    test_tree.find_by_tag("b")