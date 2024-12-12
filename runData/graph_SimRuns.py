import pandas
import matplotlib.pyplot as plt
import numpy as np

def main() :

    # test = ['gcc_x86O0_m5out', 'gcc_x86O1_m5out', 'gcc_x86O2_m5out', 'gcc_x86O3_m5out', 'gcc_ARMO0_m5out', 'gcc_ARMO1_m5out', 'gcc_ARMO2_m5out', 'gcc_ARMO3_m5out',
    #         'bzip2_x86O0_m5out', 'bzip2_x86O1_m5out', 'bzip2_x86O2_m5out', 'bzip2_x86O3_m5out', 'bzip2_ARMO0_m5out', 'bzip2_ARMO1_m5out', 'bzip2_ARMO2_m5out', 'bzip2_ARMO3_m5out']

    test = ['gcc_X86O0_m5out', 'gcc_X86O1_m5out', 'gcc_X86O2_m5out', 'gcc_X86O3_m5out',
            'bzip2_X86O0_m5out', 'bzip2_X86O1_m5out', 'bzip2_X86O2_m5out', 'bzip2_X86O3_m5out'] 

    resultsCsv = pandas.read_csv("runData/allRuns.csv", index_col=0)
    print(resultsCsv)

    # Make Graph for CPI, SimTime per benchmark

    simTime = []
    cpi = []

    # print(resultsCsv.loc['gcc_X86O0_m5out'])

    # Grab rows
    for row in test :
        simTime.append(resultsCsv.loc[row]['simSeconds'])
        # cpi.append(row['cpi'])
        pass

    print(simTime)

    xLabels = test
    width = 0.3
    x = np.arange(len(test))

    ax = plt.axes() 
    plt.bar(x, simTime, width, color='Lime')

    
    # plt.bar(x-0.3, mipsMeas, width, color='#cc2f82')
    # plt.bar(x, x86Meas, width, color='#0169b8')
    # plt.bar(x+0.3, armMeas, width, color='#0196c8')

    # plt.legend(['MIPS', 'x86', 'ARM']) 
    ax.set_yticks([0.0, 0.02, 0.04, 0.06])

    # ax.set_xticklabels(test)
    # plt.xticks(x, xLabels)

    # plt.xlabel('Adherence to Principles')
    # plt.ylabel('Percent Adherence')
    # plt.title('Adherence to Wulf\'s Principles of MIPS32, ARM-AA32, x86 ISAs')

    plt.show()

    pass

if __name__ == "__main__" :
    main()