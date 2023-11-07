def choose_func(nums: list, func1, func2):
    if sum(n < 0 for n in nums) == 0:
        return func1(nums)
    else:
        return func2(nums)


# Assertions

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return list(map(lambda x: x ** 2, nums))


def remove_negatives(nums):
    return list(filter(lambda x: x > 0, nums))


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
