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
    midMtime=[0.0, 0.0, 0.025, 0.05, 0.05, 0.075, 0.1, 0.125, 0.125, 0.175, 0.3, 0.35, 0.425, 0.5, 0.5, 0.55, 0.65, 0.725, 0.825, 0.925, 1.025, 1.125, 1.225, 1.3, 1.375, 1.5, 1.6, 1.7, 1.7, 1.85, 1.975, 2.1, 2.225, 2.325, 2.45, 2.575, 2.7, 2.85, 3.0, 3.175]
    midCtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.125, 0.125, 0.15, 0.15, 0.175, 0.175, 0.175, 0.2]
    midQtime=[0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.075, 0.1, 0.1, 0.1, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.325, 0.35, 0.425, 0.45, 0.525, 0.55, 0.55, 0.6, 0.7, 0.75, 0.825, 0.925, 1.0, 1.0, 1.075, 1.125, 1.225, 1.3]
    wrsMtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.125, 0.125, 0.125, 0.175, 0.2, 0.2, 0.2, 0.25, 0.3, 0.375, 0.475, 0.55, 0.625, 0.725, 0.85, 0.925, 1.025, 1.15, 1.25, 1.35, 1.4, 1.5, 1.625, 1.75, 1.875, 2.025, 2.15, 2.4, 2.575, 2.725, 2.925, 3.125]
    wrsCtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.125, 0.125, 0.125, 0.125, 0.15, 0.15, 0.175, 0.175, 0.2, 0.2, 0.2, 0.225, 0.225, 0.225, 0.25, 0.275, 0.3, 0.325, 0.325, 0.35, 0.35, 0.35, 0.4, 0.4, 0.4]
    wrsQtime=[0.0, 0.0, 0.0, 0.0, 0.025, 0.05, 0.075, 0.1, 0.175, 0.275, 0.275, 0.4, 0.55, 0.725, 1.05, 1.275, 1.475, 1.75, 2.0, 2.325, 2.7, 3.075, 3.475, 3.95, 4.5, 5.05, 5.65, 6.4, 7.35, 8.075, 8.825, 9.7, 10.6, 11.575, 12.6, 13.725, 14.875, 16.075, 17.35, 18.7]




    plot(midMtime, midCtime, midQtime, 'valori casuali')
    plot(wrsMtime, wrsCtime, wrsQtime, 'valori ordinati')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/