class Solution(object):
    def targetIndices(self, nums, target):
        self.arr =[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]>nums[j]):
                    nums[j],nums[i]=nums[i],nums[j]
        for i in range(len(nums)):
            if (nums[i]==target):
                self.arr.append(i)
        return self.arr