
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01

# O(NlognN)
def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            result.append(nums[i:i+3])
        return result


