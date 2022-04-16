# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy
import numpy as np

from ARN import RB as RB
from ABR import ABR as ABR
from timeit import default_timer as timer
import  matplotlib.pyplot as plt

def testInsert(abr, rb,values,ordered=(False)):
    abr=ABR()
    rb=RB()
    a=0
    r=0
    if ordered==True:
        values.sort()
    l=values[-1]
    for value in values:
      startABR=timer()
      abr.insert(value)
      timerABR=timer()-startABR
      startRB=timer()
      rb.insert(value)
      timerRB=timer()-startRB
      a+=timerABR
      r+=timerRB

    return abr,rb,a/values.size,r/values.size,l

def testFind(abr,rb,k):
    startABR = timer()
    abr.find(k)
    timerABR = timer() - startABR
    startRB = timer()
    rb.find(k)
    timerRB = timer() - startRB

    return timerABR, timerRB

def plot(abr,rb,title):
    x = np.arange(0, 1000, 100)
    y = np.arange(0)
    plt.plot(x,abr)
    plt.plot(x,rb)
    plt.title(title)
    plt.xlabel('nodes')
    plt.ylabel('time ')
    plt.legend(['ABR', 'ARN'])
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    midAbr=ABR()
    midRb=RB()
    wrsAbr = ABR()
    wrsRb = RB()
    midAbrTime=[]
    midRbTime=[]
    midAbrSearchTime=[]
    midRbSearchTime = []
    wrsAbrTime = []
    wrsRbTime = []
    wrsAbrSearchTime = []
    wrsRbSearchTime = []
    x1=0
    y1=0
    w1=0
    z1=0
    x2 = 0
    y2 = 0
    w2 = 0
    z2 = 0

    for i in range(1,1000,100):
        for j in range(40):
            values = numpy.random.randint(0, i, size=i)
            midAbr,midRb,a,r,l=testInsert(midAbr,midRb,values,False)
            x1+=a
            y1+=r
            a, r = testFind(midAbr, midRb, l)
            w1+=a
            z1+=r
            wrsAbr,wrsRb,a, r, l = testInsert(wrsAbr, wrsRb,values,True)
            x2 += a
            y2 += r
            a, r = testFind(wrsAbr, wrsRb, l)
            w2 += a
            z2 += r

        midAbrTime.append(x1/40)
        midRbTime.append(y1/40)
        midAbrSearchTime.append(w1/40)
        midRbSearchTime.append(z1/40)
        wrsAbrTime.append(x2 / 40)
        wrsRbTime.append(y2 / 40)
        wrsAbrSearchTime.append(w2 / 40)
        wrsRbSearchTime.append(z2 / 40)

    plot(midAbrTime,midRbTime,'inserimento casuale')
    plot(midAbrSearchTime,midRbSearchTime,'ricerca caso medio')
    plot(wrsAbrTime, wrsRbTime, 'inserimento ordinato')
    plot(wrsAbrSearchTime, wrsRbSearchTime, 'ricerca caso peggiore')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
