import collections


def solution(progresses, speeds):
    progresses = progresses[::-1]
    speeds = speeds[::-1]

    suc = list(zip(progresses, speeds))
    # [(55,5), (30,30), (93,1)]

    n = 1
    count = collections.defaultdict(int)
    # print(dic)

    while len(suc) != 0:

        if suc[-1][0] + suc[-1][1] * n >= 100:
            suc.pop()
            count[n] += 1
            # { '1' : 2 . '2' : 1  }
        else:
            n += 1

    return list(count.values())