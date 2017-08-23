from filter import *

def laplace(region):
    if (len(region) == 9):
        me, N, S, E, W = region[0:5]
        x = (N + S + E + W) - 4 * me
        return x
    else:
        return region[0]

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()