class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestCount = 0
        setNum= set(nums)

        

        for num in nums:
            if (num-1) not in setNum:
                count= 0
                while (num + count) in setNum:
                    count += 1
                longestCount= max(longestCount, count)

        return longestCount
        