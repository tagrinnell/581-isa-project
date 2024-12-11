import glob
import os

def main() :
    os.chdir("C:\\Users\\Taz\\Desktop\\Repos\\581-isa-project\\DataResults")
    files = glob.glob('**/*.txt', recursive=True)
    print (files)
    isaType = ['arm', 'mips32', 'x86']
    currIsa = ''

    for fileName in files :
        currIsa = ''
        # Determine what ISA we're looking at
        for isa in isaType :
            if isa in file :
                currIsa = isa

        with open(fileName, 'r') as file:
            fileContent = file.read()

        fileContent = fileContent.replace(": ", ",")

        for line in f :
            
            # Need to Change ': ' -> ,

            # Identify by instruction
            pass

if __name__ == "__main__" :
    main()