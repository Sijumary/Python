You are given a list of integers and a target value. Your task is to implement a function find_pair() that takes in the list of integers and the target value as parameters, and returns a tuple containing the indices of two elements in the list that add up to the target value. If there are multiple valid pairs, the function should return the indices of the first valid pair encountered.

from typing import List, Tuple


def find_pair(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the indices of two elements in the list that add up to the target value.
    If there are no valid pairs, the function returns an empty tuple.

    :param nums: A list of integers where each integer is within the range [-10^3, 10^3].
    :param target: An integer within the range [-10^3, 10^3].
    :return: A tuple containing two integers where 0 <= i, j <= n-1 and i != j.
    """
    # TODO: implement this function
    # Note: Do not change the existing code

    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        # Find the number needed to reach the target

        if complement in num_map:
            return (num_map[complement], i)  # Return the first valid pair found

        num_map[num] = i  # Store the index of the current number
    return ()
nums = [2, 7, 11, 15]
target = 9
print(find_pair(nums, target))
