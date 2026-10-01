class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub= nums[0]
        cursum= 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxSub = max(maxSub,cursum)
        return maxSub


        # 1st iteration:
        # maxsub = -2
        # cursum = 0

        # loop:
        # currentsum = -2
        # maxsub = -2
        # loop2:
        # currentsum is less than 0
        # current sum = 0
        # current sum = 1
        # maxsub= max(-2,1)=1

        # loop3:
        # currentsum = 1-3=-2
        # maxSub= max(1,-2)= 1

        # loop4:
        # currentsum = 0+4
        # maxsub= max(1,4) = 4

        # loop 5:
        # currentsum = 4+-1= 3
        # maxSub= max(4,3)=4

        # loop6:
        
        # currentsum = 3+2=5
        # maxsub= max(4,5)=5

        # loop7:
        # currentsum = 5+1 = 6
        # maxsub = max(4,6)= 6

        # loop8:
        # currentsum = 6-5=1
        # masxub = max(6,1)=6

        # loop 9:
        # currentsum =1+4=5
        # 6,5= 6
        





         

        