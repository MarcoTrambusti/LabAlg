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
    if(sorted==True):
       A.sort()
       #A=A[::2] + A[1::2]
       A=A[::-1]
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
    """
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

    """
    midMtime=[0.0, 0.025, 0.025, 0.05, 0.1, 0.1, 0.15, 0.175, 0.2, 0.225, 0.225, 0.25, 0.275, 0.325, 0.325, 0.4, 0.475, 0.525, 0.675, 0.75, 0.85, 0.975, 1.05, 1.15, 1.25, 1.325, 1.4, 1.55, 1.675, 1.775, 1.925, 2.05, 2.175, 2.325, 2.475, 2.475, 2.625, 2.75, 2.95, 3.1]
    midCtime=[0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.075, 0.1, 0.1, 0.1, 0.125, 0.15, 0.175, 0.175, 0.175, 0.175, 0.2, 0.2, 0.2, 0.2, 0.225, 0.225, 0.25, 0.275, 0.275, 0.275, 0.275, 0.3, 0.3, 0.3, 0.35, 0.375, 0.375, 0.4]
    midQtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.075, 0.1, 0.1, 0.125, 0.15, 0.2, 0.25, 0.325, 0.35, 0.375, 0.4, 0.475, 0.5, 0.6, 0.625, 0.675, 0.725, 0.775, 0.825, 0.9, 1.025, 1.075, 1.175, 1.175, 1.25, 1.375, 1.45, 1.5]
    wrsMtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.075, 0.1, 0.15, 0.175, 0.175, 0.225, 0.275, 0.325, 0.325, 0.4, 0.45, 0.525, 0.525, 0.6, 0.675, 0.775, 0.875, 0.95, 1.05, 1.175, 1.3, 1.375, 1.5, 1.6, 1.75, 1.875, 2.0, 2.15, 2.3, 2.8, 2.925, 3.05, 3.25, 3.45]
    wrsCtime=[0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.05, 0.05, 0.075, 0.075, 0.1, 0.1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.15, 0.15, 0.175, 0.175, 0.175, 0.175, 0.175, 0.175, 0.175, 0.175, 0.175, 0.2, 0.2, 0.2]
    wrsQtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.05, 0.1, 0.15, 0.275, 0.45, 0.575, 0.675, 0.825, 1.175, 1.35, 1.575, 1.825, 2.05, 2.35, 2.725, 3.1, 3.55, 4.05, 4.575, 5.125, 5.75, 6.425, 7.1, 7.875, 8.675, 9.55, 10.425, 11.4, 12.425, 13.425, 14.575, 15.825, 17.075, 18.425]


    plot(midMtime, midCtime, midQtime, 'inserimento casuale')
    plot(wrsMtime, wrsCtime, wrsQtime, 'inserimento caso peggiore')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/