class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates00(self, nums):
        # !! wrong answer
        lenN = len(nums)
        if lenN < 2:
            return lenN

        i, j = 0, 1
        counter = 0
        while i < lenN and j < lenN:
            if nums[j] == nums[i]:
                j += 1
                counter += 1
            elif nums[j] != nums[i] and counter > 2:
                counter = 0
                i += 2
                nums[i] = nums[j]
                j += 1
            else:
                i += 1
                j += 1
        print nums
        return i + 1

    def removeDuplicates(self, nums):
        pass



s= Solution()
nums= [1,1,1, 2,2,3]
nums1 = [1,1,2,3]
print s.removeDuplicates(nums)
