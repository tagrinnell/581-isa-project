import pandas
import matplotlib.pyplot as plt
import numpy as np

def main() :
    resultsCsv = pandas.read_csv("isa_inspection/results.csv")

    # Grab rows
    arm = resultsCsv.iloc[0]
    mips = resultsCsv.iloc[1]
    x86 = resultsCsv.iloc[2]

    armMeas = [arm['% Regular'], arm['% Orthogonal'], arm['% Composable']]
    mipsMeas = [mips['% Regular'], mips['% Orthogonal'], mips['% Composable']]
    x86Meas = [x86['% Regular'], x86['% Orthogonal'], x86['% Composable']]

    # Check grabbed information
    print(mips)
    print(arm)
    print(x86)

    xLabels = ['% Regular', '% Orthogonal', '% Composable']
    width = 0.3
    x = np.arange(len(xLabels))
    
    plt.bar(x-0.3, mipsMeas, width, color='#cc2f82')
    plt.bar(x, x86Meas, width, color='#0169b8')
    plt.bar(x+0.3, armMeas, width, color='#0196c8')

    plt.legend(['MIPS', 'x86', 'ARM']) 
    plt.xticks([0, 1, 2], xLabels)

    plt.xlabel('Adherence to Principles')
    plt.ylabel('Percent Adherence')
    plt.title('Adherence to Wulf\'s Principles of MIPS32, ARM-AA32, x86 ISAs')

    plt.show()

    pass

if __name__ == "__main__" :
    main()