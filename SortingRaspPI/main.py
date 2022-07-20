# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from CountingSort import CountingSort as CountingSort;
from MergeSort import MergeSort as MergeSort;
from QuickSort import QuickSort as QuickSort;

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [9, 6, 3, 2, 5]
    B = CountingSort(A)
    print(B)
    C= [9, 6, 3, 2, 5]
    QuickSort(C,0,(len(C)-1))
    print(C)
    C = [9, 6, 3, 2, 5]
    MergeSort(C,0,(len(C)-1))
    print(C)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
