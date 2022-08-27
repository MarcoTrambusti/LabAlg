# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
#from timeit import default_timer as timer
import math;
from utime import sleep

def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+j+1]
    L[n1]=float('inf')
    R[n2]=float('inf')
    i=0
    j=0

    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1

def MergeSort(A,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
        
def CountingSort(A):
  k = max(A)
  B = [0] * len(A)
  C = [0]*(k+1)
  #for i in range(k + 1):
    #C.append(0)
  for j in range(len(A)):
    C[A[j]] = C[A[j]] + 1
  for i in range(1,(k+1)):
    C[i] = C[i] + C[i - 1]
  for j in range((len(A) - 1), -1, -1):
    B[(C[A[j]] - 1)] = A[j]
    C[A[j]] = C[A[j]] - 1

  return B;

def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def QuickSort(A,p,r):
    if len(A)==1:
        return A
    if p<r:
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)


def test(A, sorted=False):
    if(sorted==True):
      A.sort()
      A=A[::-1]
      
    D=A.copy()
    C=A.copy()
    startQ = time.time()
    QuickSort(D, 0, len(D) - 1)
    timerQ = time.time() - startQ
    startM =time.time()
    MergeSort(C, 0, len(C) - 1)
    timerM = time.time() - startM
    startC = time.time()
    B = CountingSort(A)
    timerC = time.time()- startC

    #if (B == C):
        #if (C == D):
    return timerM, timerC, timerQ


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("ciao")
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
        print(i)
        for j in range(40):
            A =[]
            for n in range(i):
              A.append(random.randint(0,100))
            mM, mC,mQ= test(A,True)
            xm += mM
            xc += mC
            xq += mQ
        midMtime.append(xm / 40)
        midCtime.append(xc / 40)
        midQtime.append(xq / 40)

    #plot(midMtime, midCtime, midQtime, 'inserimento casuale')
    print("fgefe",midMtime)
    print(midCtime)
    print(midQtime)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

