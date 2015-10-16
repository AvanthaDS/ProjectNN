__author__ = 'Avantha'


class tst:
    def __init__(self, lst, val):
        self.lst1 = lst
        self.ve = val
        print(self.lst1)
        print(self.ve)


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(chunkIt(l, 3))

ads = tst(l, 5)
