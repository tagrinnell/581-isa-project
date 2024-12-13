import pandas
import matplotlib.pyplot as plt
import numpy as np

def main() :

    # test = ['gcc_x86O0_m5out', 'gcc_x86O1_m5out', 'gcc_x86O2_m5out', 'gcc_x86O3_m5out', 'gcc_ARMO0_m5out', 'gcc_ARMO1_m5out', 'gcc_ARMO2_m5out', 'gcc_ARMO3_m5out',
    #         'bzip2_x86O0_m5out', 'bzip2_x86O1_m5out', 'bzip2_x86O2_m5out', 'bzip2_x86O3_m5out', 'bzip2_ARMO0_m5out', 'bzip2_ARMO1_m5out', 'bzip2_ARMO2_m5out', 'bzip2_ARMO3_m5out']

    test = ['gcc_X86O0_m5out', 'gcc_X86O1_m5out', 'gcc_X86O2_m5out', 'gcc_X86O3_m5out',
            'bzip2_X86O0_m5out', 'bzip2_X86O1_m5out', 'bzip2_X86O2_m5out', 'bzip2_X86O3_m5out'] 
    labels = ["gcc - Opt. 0", "gcc - Opt. 1", "gcc - Opt. 2", "gcc - Opt. 3",
              "bzip2 - Opt. 0", "bzip2 - Opt. 1", "bzip2 - Opt. 2", "bzip2 - Opt. 3"]
              
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
    width = 0.5
    x = np.arange(len(test))

    ax = plt.axes() 
    barlist = plt.bar(labels, simTime, width, color='#0169b8')#, hatch=['/', '/', '/', '/', 'o', 'o', 'o', 'o']) # '/', '.', '-', '|'

    ax.tick_params(axis='x', labelrotation=70)
    plt.legend(['x86'])

    plt.xlabel('Optimization Level')
    plt.ylabel('Simulated Runtime (secs)')
    plt.title('Simulated Runtime by Benchmark')
    plt.tight_layout()

    plt.show()

    pass

if __name__ == "__main__" :
    main()