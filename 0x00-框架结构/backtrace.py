# -*- coding: utf-8 -*-

"""
回溯算法解题思路框架
1. 全排列问题
2. N皇后问题
"""


class Permute:
    """
    全排列问题demo
    """

    def __init__(self):
        self._result = []

    def entrance(self, nums: [int]) -> [int]:
        track = []
        self.backtrack(nums, track)
        return self._result

    def backtrack(self, nums: [int], track: [int]):
        if len(track) == len(nums):
            self._result.append(track.copy())
            return

        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrack(nums, track)
            track.pop()


if __name__ == "__main__":
    p = Permute()
    res = p.entrance([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("count: ", len(res))
