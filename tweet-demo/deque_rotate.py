from collections import deque


def rotate(numbers: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    numbers_deque = deque(numbers)
    numbers_deque.rotate(k)
    numbers[:] = numbers_deque


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)  # [5, 6, 7, 1, 2, 3, 4]
