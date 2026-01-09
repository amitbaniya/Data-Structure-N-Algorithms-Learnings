from collections import deque

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}

        for i in range(0, len(nums)):
            dict[nums[i]] = i

        for i in range(0, len(nums)):
            second_number = target - nums[i]
            if second_number in dict:
                if dict[second_number] != i:
                    return [i, dict[second_number]]
                    break

if __name__ == '__main__':
    sl = Solution()

    print(sl.twoSum([1,2,3], 4))
    print(sl.twoSum([2, 7, 11, 13, 14], 9))




