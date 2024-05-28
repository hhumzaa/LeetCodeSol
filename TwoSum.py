class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        matches all numbers to their index (latest index if same num appears twice in nums, 
        this is fine as we can not use same element twice)
        Time complexity: O(n)
        Space complexity: O(n)
        """
        hNums = {}
        for i in range(len(nums)):
            hNums[nums[i]] = i

        """ 
        iterate over all nums, at each iteration fix one number and check if the other exists in the hashmap
        Time complexity: O(n)
        """
        for i in range(len(nums)):
            numToFind = target - nums[i]
            if numToFind in hNums and i != hNums[numToFind]:
                return [i, hNums[numToFind]]
        return [] 
        """
        Time complexity: O(n) + O(n) = O(2n) = O(n) // since constants ignored in Big O notation
        Space complexity: O(n)
        """