# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    # 1 copy to new array
    # 2 circular linkedlist?
    def rotate0(self, nums, k):
        """
        use another array space
        """
        ret = []
        if nums== []:
            return []
        # k < 0 ?
        k = k % len(nums)
        if k == 0:
            return nums
        # why 1st impression to use k + 1?
        for i in xrange(len(nums)-k, len(nums)):
            ret.append(nums[i])
        for i in xrange(len(nums)-k):
            ret.append(nums[i])
        return ret

    def rotate1(self, nums, k):
        """
        python specific list slice and append
        """
        ret = []
        if nums== []:
            return []
        # k < 0 ?
        k = k % len(nums)
        if k == 0:
            return nums
        # why 1st impression to use k + 1?
        ret = nums[len(nums)-k :] + nums[:len(nums)-k]
        # for i in xrange(len(nums)-k, len(nums)):
        #     ret.append(nums[i])
        #
        # for i in xrange(len(nums)-k):
        #     ret.append(nums[i])
        return ret

    def rotate(self, nums, k):
        """
        3 reverse to array
        """
        if nums== []:
            return
        # k < 0 ?
        k = k % len(nums)
        if k == 0:
            return
        self.rev_arr2(nums, 0, len(nums)-1)
        self.rev_arr2(nums, 0, k-1)
        self.rev_arr2(nums, k, len(nums)-1)
        print nums

    def rotate2(self, nums, k):
        """
        intuitive way to rotate 1 step for every element, then for k steps
        """

        # 1 rotate all element one step for one loop
        # 2 rotate one element for k step, then another element
        if nums== []:
            return
        # k < 0 ?
        k = k % len(nums)
        if k == 0:
            return

        """
        # how to loop from start to end?
        last_el = nums[-1]
        for i in xrange(1, len(nums)-1):
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i+1] = temp
        nums[0] = last_el
        """
        for j in xrange(k):
            i = len(nums) -1
            last_el = nums[i]
            while i > 0:
                nums[i] = nums[i-1]
                i -= 1
            nums[0] = last_el
        print nums

# 1 2 3 4 5 6 7
# 4     1
#

    def rotate3(self, nums, k):
        """
        for every element, rotate it for k step
        Another way: use hashmap
        """
        if nums== []:
            return
        # k < 0 ?
        k = k % len(nums)
        if k == 0:
            return

        idx = 0
        cur = nums[0]
        distance = 0
        for x in xrange(len(nums)):
            next = (idx + k) % len(nums)
            temp = nums[next]
            nums[next] = cur
            cur = temp
            idx = next

            distance = (distance + k) % len(nums)
            if distance == 0:
                idx = (idx + 1) % len(nums)
                cur = nums[idx]


        print nums


    def rev_arr(self, nums, start, end):
        # this loop condition is nice!
        # my first idea, is like length/2
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end]= temp
            start += 1
            end -= 1

    def rev_arr2(self, nums, start, end):
        # use XOR to swap data without temp
        while start < end:
            nums[start] ^= nums[end]
            nums[end] ^= nums[start]
            nums[start] ^= nums[end]
            start, end = start+1, end-1

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def gcd2(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def fab(self, n):
        a, b = 0, 1
        i = 0
        while i < n:
            a, b = b, a+b
            i += 1
            print a


a = Solution()
#print a.rotate1([1,2,3,4,5,6,7], 8)
#                5,6,7,1,2,3,4
a.rotate2([1], 0)
# nums = [1,2,3,4,5,6,7]
# a.rev_arr(nums, 0, 6)
# print nums
#print a.rotate([1,2,3,4,5,6,7], 2)

#print a.gcd2(9, 12)

#a.fab(10)

a.rotate3([1,2,3,4,5,6,7], 2)

