class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero= 0
        i = 0
        while i < len(nums):
            if nums[i]== 0:
                count_zero +=1
            else:
                product *= nums[i]
            i +=1
    
        res= []
        for i in nums:
            if count_zero >= 2:
                res.append(0)
            elif count_zero == 1:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
                
            else:
                res.append(product//i)
        return res
