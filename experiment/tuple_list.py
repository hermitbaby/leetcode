from string import ascii_lowercase
from random import randint
from timeit import Timer


def check_index(st, guesses):
    for i in guesses:
        idx = st.index(i)

if __name__ == "__main__":
    num_checks = 10
    lst = [n for n in ascii_lowercase]
    st = ascii_lowercase
    tup = tuple(lst)
    guesses = [ascii_lowercase[randint(0, len(ascii_lowercase)-1)]
               for n in xrange(num_checks)]

    print guesses

    def run_string():
        check_index(st, guesses)

    def run_list():
        check_index(lst, guesses)

    def run_tuple():
        check_index(tup, guesses)

    # 1 million times
    t2 = Timer(run_list)
    print "List", t2.timeit()
    t3 = Timer(run_tuple)
    print "Tuple", t3.timeit()
    t = Timer(run_string)
    print "String", t.timeit()

