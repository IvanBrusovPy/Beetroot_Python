from typing import Optional

from collections import deque


class Tree:

    def __init__(self, tag="<!DOCTYPE html>", value=""):
        self.tag = tag
        self.value = value
        self.parent = None
        self.child = []

    def add_child(self, tag, value):
        new_child = Tree(tag, value)
        new_child.parent = self
        self.child.append(new_child)
        return self

    def print_tree(self, level=0):
        ret = f"{'   '*level} {self.tag}  {self.value} \n"
        for c in self.child:
            ret += c.print_tree(level + 1)
        return ret

    def to_parent(self):
        if self.parent is not None:
            return self.parent
        else:
            return self

    def to_child(self):
        return self.child[len(self.child)-1]

    def parseHTML(self, file_path):

        with open(file_path) as f:
            lines = f.read()

        tags = [""]
        texts = [""]
        temp_tag = ""
        add = False
        a = self
        for i in lines:


            if i == "<":
                add = True

            if add is False:
                texts[len(texts) - 1] += i

            if i == ">":
                add = False
                temp_tag += ">"
                if temp_tag.replace("/", "") == tags[len(tags)-1]:
                    a.add_child(temp_tag.replace("/", ""), texts[len(texts) - 1].replace("\n", ""))
                    del tags[len(tags) - 1]
                    del texts[len(texts) - 1]
                else:
                    tags.append(temp_tag)
                    texts.append("")
                temp_tag = ""
            if add:
                temp_tag += i

    def find_by_tag(self, find_tag):
        if self.tag == "<"+find_tag+">" and self.value != "":
            print(self.tag, self.value)
        for c in self.child:
            c.find_by_tag(find_tag)


