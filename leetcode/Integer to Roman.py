# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        transTable = {
            1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'
        }

        result = ''
        for key in sorted(transTable.keys())[::-1]:
            while num != 0 and num >= key:
                num -= key
                result += transTable[key]
            if num == 0:
                break


        # # 900, 400, 90, 40, 9, 4
        simplifyTable = {
            'DCCCC': 'CM', 'CCCC': 'CD', 'LXXXX': 'XC', 'XXXX': 'XL', 'VIIII': 'IX', 'IIII': 'IV'
        }
        simplifyStr = ['DCCCC', 'CCCC', 'LXXXX', 'XXXX', 'VIIII', 'IIII']

        for simplify in simplifyStr:
            if simplify in result:
                # print result, simplify
                result = result.replace(simplify, simplifyTable[simplify])
                # print result

        return result


s= Solution()
print s.intToRoman(9)
