import random
import time

from QuickSort import QuickSort
from MergeSort import MergeSort
from CountingSort import CountingSort
import sys

def test(A, sorted=False):
    if (sorted == True):
        A.sort()

    D = A.copy()
    C = A.copy()
    startQ = time.time()
    QuickSort(D, 0, len(D) - 1)
    timerQ = time.time() - startQ
    startM = time.time()
    MergeSort(C, 0, len(C) - 1)
    timerM = time.time() - startM
    startC = time.time()
    B = CountingSort(A)
    timerC = time.time() - startC

    if (B == C):
      if (C == D):
       return timerM, timerC, timerQ


def RunTests():
    xm = 0
    xc = 0
    xq = 0
    ym = 0
    yc = 0
    yq = 0
    midMtime = []
    midCtime = []
    midQtime = []
    wrsMtime = []
    wrsCtime = []
    wrsQtime = []
    for i in range(1, 400, 10):
        for j in range(40):
            A = []
            for n in range(i):
                A.append(random.randint(0, 100))
            B = A.copy()
            mM, mC, mQ = test(A, False)
            wM, wC, wQ = test(B, True)
            xm += mM
            xc += mC
            xq += mQ
            ym += wM
            yc += wC
            yq += wQ
        midMtime.append(xm / 40)
        midCtime.append(xc / 40)
        midQtime.append(xq / 40)
        wrsMtime.append(ym / 40)
        wrsCtime.append(yc / 40)
        wrsQtime.append(yq / 40)
    return  midMtime,wrsMtime,midCtime,wrsCtime,midQtime,wrsQtime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    midMtime,wrsMtime,midCtime,wrsCtime,midQtime,wrsQtime=RunTests()

    print("caso Medio:")
    print(midMtime)
    print(midCtime)
    print(midQtime)
    print("caso Peggiore:")
    print(wrsMtime)
    print(wrsCtime)
    print(wrsQtime)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

