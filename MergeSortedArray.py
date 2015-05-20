# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge00(self, nums1, m, nums2, n):
        """
        loop through nums1 or nums2 first?
        this method has bug!!
        1 insert element of nums2 into nums1(use insert method of list)
            problem is : the length of nums1 is already m+n, so can't use insert
        2 use temp array then copy them to nums1
        3 add element in nums1 from back
        """
        i, j = 0, 0
        while i < m + n and j < n:
            print i, j
            if i < m and nums2[j] > nums1[i]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                print nums1
                j += 1
                i += 1
            # if i >= m and j==0:
            #     print nums1
            #     nums1.insert(i, nums2[j])
            #     j += 1
            #     i += 1

    def merge(self, nums1, m, nums2, n):
        lastN = n-1
        lastM = m-1
        last2write = m + n - 1
        if m == 0:
            nums1[:] = nums2[:]
            print nums1
            return

        while lastN >= 0 and lastM >= 0:
            if nums1[lastM] >= nums2[lastN]:
                nums1[last2write] = nums1[lastM]
                lastM -= 1
            else:
                nums1[last2write] = nums2[lastN]
                lastN -= 1
            last2write -= 1
        if lastM == -1:
            nums1[:lastN+1] = nums2[:lastN+1]
        # print nums1



s = Solution()
s.merge([1, 2,3,4, 10, 20, 0 , 0,0 , 0], 6, [4, 5, 6, 22], 4)
s.merge([0], 0, [1], 1)
