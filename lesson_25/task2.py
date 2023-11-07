from stack import Stack


def balanced_brackets(line: str):
    brackets = Stack()
    for i in line:
        if i == "{" or i == "(":
            brackets.push(i)
        if i == "}" and brackets.peek() == "{" or i == ")" and brackets.peek() == "(":
            brackets.pop()

    return brackets.is_empty()


if __name__ == '__main__':
    assert balanced_brackets('abc{cbg{dfgfgh}5464(34)}b') == True
    assert balanced_brackets('abc{cbg{dfg34)}b') == False
