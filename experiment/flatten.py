# -*- coding: utf-8 -*-
from rcviz import callgraph, viz


# turn [1, [2, [3,4]], 5] to [1,2,3,4,5]
flat = list()

@viz
def flatten_in(arr, flat):
    for i in arr:
        flatten_in.track(i=i)
        flatten_in(i, flat) if isinstance(i, list) else flat.append(i)
    return flat

nested = [1, [2, [3,4]], 5]
flatten_in(nested, flat)
callgraph.render("pic/flatten.svg")