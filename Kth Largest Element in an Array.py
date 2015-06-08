# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 <= k <= array's length.


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        """
        sorting algorithm
           1 O(n * logN)
                built-in sorting algo
           2 QuickSelect algorithm
                O(n)
           3 min priority queue
                O(n * logK)
        """
        import heapq
        heapq.heapify(nums)
        # print nums
        for i in xrange(len(nums) - k):
            heapq.heappop(nums)
        res = heapq.heappop(nums)
        # res = heapq.nlargest(k, nums)

        return res


s = Solution()
nums = [3,2,1,5,6,4]
print s.findKthLargest(nums, 2)




