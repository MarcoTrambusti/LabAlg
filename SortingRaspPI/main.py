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
       #A=A[::-1]
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

    if (B == C):
        if (C == D):
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
        print(i)
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

    midMtime, wrsMtime, midCtime, wrsCtime, midQtime, wrsQtime = RunTests()


    midMtime=[0.0, 0.0, 0.025, 0.05, 0.05, 0.075, 0.1, 0.125, 0.125, 0.175, 0.3, 0.35, 0.425, 0.5, 0.5, 0.55, 0.65, 0.725, 0.825, 0.925, 1.025, 1.125, 1.225, 1.3, 1.375, 1.5, 1.6, 1.7, 1.7, 1.85, 1.975, 2.1, 2.225, 2.325, 2.45, 2.575, 2.7, 2.85, 3.0, 3.175]
    midCtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.125, 0.125, 0.15, 0.15, 0.175, 0.175, 0.175, 0.2]
    midQtime=[0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.075, 0.1, 0.1, 0.1, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.325, 0.35, 0.425, 0.45, 0.525, 0.55, 0.55, 0.6, 0.7, 0.75, 0.825, 0.925, 1.0, 1.0, 1.075, 1.125, 1.225, 1.3]
    wrsMtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.125, 0.125, 0.125, 0.175, 0.2, 0.2, 0.2, 0.25, 0.3, 0.375, 0.475, 0.55, 0.625, 0.725, 0.85, 0.925, 1.025, 1.15, 1.25, 1.35, 1.4, 1.5, 1.625, 1.75, 1.875, 2.025, 2.15, 2.4, 2.575, 2.725, 2.925, 3.125]
    wrsCtime=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025, 0.025, 0.025, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.125, 0.125, 0.125, 0.125, 0.15, 0.15, 0.175, 0.175, 0.2, 0.2, 0.2, 0.225, 0.225, 0.225, 0.25, 0.275, 0.3, 0.325, 0.325, 0.35, 0.35, 0.35, 0.4, 0.4, 0.4]
    wrsQtime=[0.0, 0.0, 0.0, 0.0, 0.025, 0.05, 0.075, 0.1, 0.175, 0.275, 0.275, 0.4, 0.55, 0.725, 1.05, 1.275, 1.475, 1.75, 2.0, 2.325, 2.7, 3.075, 3.475, 3.95, 4.5, 5.05, 5.65, 6.4, 7.35, 8.075, 8.825, 9.7, 10.6, 11.575, 12.6, 13.725, 14.875, 16.075, 17.35, 18.7]
    """
    midMtime=[0.0, 0.0, 7.49826431274414e-05, 0.0001500248908996582, 0.0001750171184539795, 0.0001750171184539795, 0.00029948949813842776, 0.0005240261554718018, 0.0007496356964111328, 0.0008490324020385742, 0.0014242589473724364, 0.0015748083591461183, 0.0018504858016967773, 0.0022019803524017333, 0.002602165937423706, 0.003027516603469849, 0.0033795475959777833, 0.003778254985809326, 0.004077816009521484, 0.0045522570610046385, 0.005027693510055542, 0.005526411533355713, 0.006178534030914307, 0.006752902269363403, 0.007326638698577881, 0.00782586932182312, 0.008500170707702637, 0.009249567985534668, 0.009973794221878052, 0.010697543621063232, 0.01147085428237915, 0.01229650378227234, 0.013146209716796874, 0.014020407199859619, 0.015020233392715455, 0.015996164083480834, 0.01692415475845337, 0.017923885583877565, 0.018949943780899047, 0.019974762201309205]
    midCtime=[0.0, 0.0, 0.0, 0.0, 9.996294975280761e-05, 9.996294975280761e-05, 0.00012503862380981446, 0.00012503862380981446, 0.00012503862380981446, 0.00017510056495666503, 0.00025007724761962893, 0.0003250479698181152, 0.0003250479698181152, 0.0004256188869476318, 0.00047633647918701174, 0.0005507051944732666, 0.0006250202655792237, 0.0006493210792541503, 0.0006493210792541503, 0.0006493210792541503, 0.0007738173007965088, 0.0008483946323394776, 0.0008734166622161865, 0.0009234309196472168, 0.0009234309196472168, 0.0010239601135253907, 0.0010991811752319336, 0.0011742293834686279, 0.0012492299079895019, 0.0013740479946136475, 0.0013990402221679688, 0.0014735221862792968, 0.0015479326248168945, 0.0016229093074798585, 0.0016730189323425292, 0.0017230451107025147, 0.0018238246440887452, 0.001873856782913208, 0.0019487857818603516, 0.0019996166229248047]
    midQtime=[0.0, 2.574920654296875e-05, 5.074739456176758e-05, 5.074739456176758e-05, 0.00010074377059936524, 0.00010074377059936524, 0.0001257479190826416, 0.00015126466751098634, 0.0003011882305145264, 0.00035117268562316893, 0.00047610998153686525, 0.0005011022090911865, 0.0006516754627227783, 0.0007780134677886963, 0.0009779155254364014, 0.0011296391487121582, 0.0013538599014282227, 0.0015532016754150391, 0.0017787039279937745, 0.0020782113075256347, 0.002253204584121704, 0.002453714609146118, 0.002628713846206665, 0.0027787387371063232, 0.003104442358016968, 0.0035045921802520754, 0.0037785589694976805, 0.004028493165969848, 0.004278510808944702, 0.004603725671768188, 0.004903334379196167, 0.005228054523468017, 0.005653256177902221, 0.00607866644859314, 0.0063790977001190186, 0.006877934932708741, 0.0073021650314331055, 0.007776564359664917, 0.008201426267623902, 0.008625882863998412]
    wrsMtime=[0.0, 4.9960613250732425e-05, 7.495880126953124e-05, 0.00014994144439697265, 0.00024998784065246584, 0.00034999847412109375, 0.0005256593227386475, 0.000775223970413208, 0.0009001791477203369, 0.0011497795581817626, 0.0015233933925628662, 0.0018227994441986084, 0.002123945951461792, 0.0024227678775787355, 0.0027476847171783447, 0.0031491398811340334, 0.0035993635654449465, 0.003924185037612915, 0.004174256324768066, 0.004674869775772095, 0.005174314975738526, 0.00567435622215271, 0.006272739171981812, 0.006823915243148804, 0.0074482977390289305, 0.007900220155715943, 0.008525139093399048, 0.009048986434936523, 0.009699606895446777, 0.010449355840682984, 0.011126172542572022, 0.012052357196807861, 0.013027578592300415, 0.013928091526031494, 0.014802831411361694, 0.015806007385253906, 0.016780215501785278, 0.017756837606430053, 0.018781322240829467, 0.019931739568710326]
    wrsCtime=[0.0, 2.4241209030151367e-05, 2.4241209030151367e-05, 4.92393970489502e-05, 4.92393970489502e-05, 7.423758506774902e-05, 9.914636611938477e-05, 9.914636611938477e-05, 9.914636611938477e-05, 0.00012413859367370604, 0.0002490580081939697, 0.0002740621566772461, 0.0002997636795043945, 0.000400543212890625, 0.0004255056381225586, 0.0004998743534088135, 0.0005248486995697021, 0.0006000816822052002, 0.0007250010967254639, 0.0007500052452087402, 0.0007999837398529053, 0.0008748948574066162, 0.0009499013423919678, 0.0010249197483062744, 0.001074928045272827, 0.001224374771118164, 0.0013735294342041016, 0.0014988958835601806, 0.001598912477493286, 0.0017739295959472655, 0.0018988609313964843, 0.0019232988357543944, 0.0019733130931854246, 0.0020483672618865968, 0.0021984100341796873, 0.0022734761238098144, 0.002322942018508911, 0.0023729562759399413, 0.002497941255569458, 0.002597898244857788]
    wrsQtime=[0.0, 0.0, 2.4998188018798827e-05, 0.00010000467300415039, 0.0001750051975250244, 0.0005505740642547608, 0.0007754981517791748, 0.0010509252548217773, 0.0014504313468933106, 0.002025413513183594, 0.0033765792846679687, 0.004177391529083252, 0.004974925518035888, 0.005921995639801026, 0.007096868753433227, 0.008469748497009277, 0.009944510459899903, 0.011646974086761474, 0.01369619369506836, 0.015821617841720582, 0.017971789836883544, 0.020423001050949095, 0.023022407293319704, 0.02592148780822754, 0.02917293906211853, 0.03267279863357544, 0.03635016083717346, 0.04037595987319946, 0.044650989770889285, 0.04915279746055603, 0.05417856574058533, 0.05945282578468323, 0.06495268940925598, 0.07082772254943848, 0.07717764973640442, 0.08384897708892822, 0.09094800353050232, 0.09839776158332825, 0.10624814033508301, 0.11459757685661316]


    plot(midMtime, midCtime, midQtime, 'valori casuali')
    plot(wrsMtime, wrsCtime, wrsQtime, 'valori ordinati')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/