# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        """
        the initial number is 1, fixed; n just means index n
        """
        if n == 0:
            return ''
        nums = []
        nums.append('1')
        for i in xrange(1, n):
            temp = []
            cur_num_str = nums[i-1]
            digit_count = 1
            # if len(cur_num_str) == 1:
            #     temp.append('1' + cur_num_str[0])
            for j in xrange(1, len(cur_num_str)):
                if cur_num_str[j] == cur_num_str[j-1]:
                    digit_count += 1
                else:
                    temp.append(str(digit_count) + cur_num_str[j-1])
                    digit_count = 1
            temp.append(str(digit_count) + cur_num_str[-1])
            temp_num_str = ''.join(temp)
            nums.append(temp_num_str)
        # print nums
        return nums[-1]


s = Solution()
print s.countAndSay(5)
