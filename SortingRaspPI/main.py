# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from CountingSort import CountingSort as CountingSort
from MergeSort import MergeSort as MergeSort
from QuickSort import QuickSort as QuickSort


def test(A, sorted=False):
    #if(sorted==True):
      #  A.sort()
       # A=A[::-1]
    D=A.copy()
    C=A.copy()
    startQ = timer()
    QuickSort(D, 0, len(D) - 1)
    timerQ = timer() - startQ
    startM = timer()
    MergeSort(C, 0, len(C) - 1)
    timerM = timer() - startM
    startC = timer()
    B = CountingSort(A)
    timerC = timer() - startC

    if (B == C).all():
        if (C == D).all():
            return timerM, timerC, timerQ


def plot(merge, counting, quick, title):
    x = np.arange(0, 4000, 100)
    y = np.arange(0)
    plt.plot(x, merge)
    plt.plot(x, counting)
    plt.plot(x, quick)
    plt.title(title)
    plt.xlabel('nodes')
    plt.ylabel('time ')
    plt.legend(['MERGE SORT', 'COUNTING SORT', 'QUICK SORT'])
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [9, 6, 3, 2, 5]
    B = CountingSort(A)
    print(B)
    C = [9, 6, 3, 2, 5]
    QuickSort(C, 0, (len(C) - 1))
    print(C)
    C = [9, 6, 3, 2, 5]
    MergeSort(C, 0, (len(C) - 1))
    print(C)
    xm = 0
    xc = 0
    xq = 0
    midMtime = []
    midCtime = []
    midQtime = []

    for i in range(1, 400, 10):
        for j in range(40):
            A = np.random.randint(100, size=i)
            mM, mC, mQ= test(A,True)
            xm += mM
            xc += mC
            xq += mQ
        midMtime.append(xm / 40)
        midCtime.append(xc / 40)
        midQtime.append(xq / 40)

    plot(midMtime, midCtime, midQtime, 'inserimento casuale')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
