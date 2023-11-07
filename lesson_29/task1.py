from random import randint


def double_side_bubble_sort(array: list):
    while True:
        swap_counter = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap_counter += 1
        for i in range(len(array)-1, 1, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                swap_counter += 1
        if swap_counter == 0:
            return array

# Є ефективним для перенесення елементів з протилежних частей масиву.
# (якщо найменші елементи стоять у кінці, а найбільші - напочатку)


if __name__ == "__main__":
    a = [randint(0, 100) for _ in range(50)]
    print(a)
    print(double_side_bubble_sort(a))
