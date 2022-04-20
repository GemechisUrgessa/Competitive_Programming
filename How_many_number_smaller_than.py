class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        self.result = []
        self.count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]> nums[j]):
                    self.count+=1
            self.result.append(self.count)
            self.count = 0
        return self.result