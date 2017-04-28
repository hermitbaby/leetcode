# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
import timeit
import os
import sys
from pympler import asizeof
import operator
import collections

class Solution:

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
              73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

    alphabet_and_quote = map(chr, range(ord('a'), ord('z') + 1)) + ["'"]

    alphabet_and_quote2 = list("etaoinshrdlcumwfgypbvkjxqz") + ["'"]

    letter_prime_map = dict(zip(alphabet_and_quote2, primes[:len(alphabet_and_quote)]))


    def get_data_from_file(self):
        print os.path.getsize('anagrams_wordlist.txt')

        word_list = []
        with open('anagrams_wordlist.txt', 'r') as f:
            # for line in f:
            #     word_list.append(line)
            word_list = f.read().splitlines()

        return word_list


    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict = {}

        for item in strs:
            key = ''.join(sorted(item))
            if key not in dict:
                dict[key] = [item]
            else:
                dict[key] += [item]

        print str(sys.getsizeof(dict)/1000) + ' KB'
        # with open("anagrams_wordlist_size.txt", "w") as text_file:
        #     text_file.write(asizeof.asized(dict, detail=2).format())

        result = set()
        for key in dict:
            if len(dict[key]) > 1:
                # flat list
                # result.extend(dict[key])
                # list of list
                result.add(frozenset(dict[key]))
        return result

    # read from file
    def anagrams2(self, word_list):

        # print (word_list)
        # print sys.getsizeof(word_list)

        res = collections.defaultdict(set)
        for s in word_list:
            product = self.calc_product(s)
            # res[product] += [s]
            res[product].add(s)

        result = { frozenset(res[key]) for key in res if len(res[key]) > 1 }

        return result

    def calc_product(self, sstr):

        nums = []
        for s in sstr:
            if s.lower() not in Solution.letter_prime_map:
                raise Exception(s.lower())
                # print s.lower()
                # return
            # num_idx = Solution.alphabet_and_quote.index(s.lower())
            # num = Solution.primes[num_idx]

            num = Solution.letter_prime_map.get(s.lower())
            nums.append(num)

        # reduce(operator.mul, nums)
        product = reduce(lambda x, y: x * y, nums)
        return product



s = Solution()
# print s.letter_prime_map

# word_list = s.anagrams2()
data = s.get_data_from_file()

start = timeit.default_timer()
res2 = s.anagrams2(data)
print len(res2)
# with open("anagrams_wordlist_res.txt", "w") as text_file:
#     text_file.write(str(res2))
stop = timeit.default_timer()
print stop - start

start = timeit.default_timer()
res = s.anagrams(data)
print len(res)
stop = timeit.default_timer()
print stop - start

print res2 - res
# print res
# print res
# print sys.getsizeof(res)

# print asizeof.asized(dict, detail=1).format()
