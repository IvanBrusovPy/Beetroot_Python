from typing import List, Tuple


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:  # O(n)
        if el_first_list in second_list:  # O(1)
            res.append(el_first_list)  # O(1)
    return res
    # O(n)


def question2(n: int) -> int:
    for _ in range(10):  # O(1)
        n **= 3  # O(1)
    return n
    # O(1)


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:  # O(n)
        flag = False
        for check in temp:  # O(n)
            if el_second_list == check:  # O(1)
                flag = True
                break
        if not flag:  # O(1)
            temp.append(second_list)
    return temp
    # O(n^2)


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:  # O(n)
        if el > res:
            res = el
    return res
    # O(n)


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            res.append((i, j))  # O(1)
    return res
    # O(n^2)


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
    # O(log n)
