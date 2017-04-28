


def get_percentile(time_list):
    """
    1 sort the raw data
    2 get the index = length(list) * 90%
    3 check whether index is integer or not
    """
    import math
    time = sorted(time_list)
    index = (len(time) - 1 ) * 0.9

    if type(index) == int:
        return time(int(index))
    else:
        left = time(int(math.floor(index))) * (math.ceil(index) - index)
        right = time(int(math.ceil(index))) * abs((math.floor(index) - index))
        return left + right

