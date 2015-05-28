# Given a digit string, return all possible letter combinations that the number could represent.
#
# # A mapping of digit to letters (just like on the telephone buttons) is given below.
# 0   ' '
# 1   ''
# 2   'abc'
# 3   'def'
# 4   'ghi'
# 5   'jkl'
# 6   'mno'
# 7   'pqrs'
# 8   'tuv'
# 9   'wxyz'



class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations0(self, digits):
        """
        Also can solve in recursive way
        """

        dict = {
            '0':  ' ',
            '1':  '',
            '2':  'abc',
            '3':  'def',
            '4':  'ghi',
            '5':  'jkl',
            '6':  'mno',
            '7':  'pqrs',
            '8':  'tuv',
            '9':  'wxyz'
        }

        strs = []
        for d in digits:
            strs.append(dict[d])

        cur_comb = []
        pre_comb = []
        for i in xrange(len(strs)):
            if i == 0:
                # Or pre_comb = list(strs[0])
                pre_comb[:] = strs[0]
                # for s in strs[i]:
                #     pre_comb.append(s)
            else:
                for j in xrange(len(pre_comb)):
                    for s in strs[i]:
                        cur_comb.append(pre_comb[j] + s)
                pre_comb = cur_comb
                cur_comb = []

        return pre_comb

    def letterCombinations(self, digits):
        dict = {
            '0':  ' ',
            '1':  '',
            '2':  'abc',
            '3':  'def',
            '4':  'ghi',
            '5':  'jkl',
            '6':  'mno',
            '7':  'pqrs',
            '8':  'tuv',
            '9':  'wxyz'
        }



        def dfs(idx, string, result, mycount):
            # print string
            print str(mycount)
            mycount += 1
            if idx == length:
                result.append(string)
                return
            for letter in dict[digits[idx]]:
                print 'dfs - ' + str(mycount) + '(',  str(idx), (string + letter), result, " )"
                dfs(idx+1, string + letter, result, mycount)


        mycount = 0
        result = []
        length = len(digits)
        dfs(0, '', result, mycount)
        return result


s = Solution()
print s.letterCombinations('345')