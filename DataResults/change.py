import glob
import os

def recursiveParse() :
    # os.chdir("C:\\Users\\Taz\\Desktop\\Repos\\581-isa-project\\DataResults")
    os.chdir("/home/taz/Repos/581-isa-project/DataResults")
    files = glob.glob('**/*.txt', recursive=True)
    print (files)
    isaType = ['arm', 'mips32', 'x86']
    currIsa = ''

    for fileName in files :
        currIsa = ''    
        # Determine what ISA we're looking at
        for isa in isaType :
            if fileName.find(isa) != -1 :
                currIsa = isa

        with open(fileName, 'r') as file:
            with open(fileName + "_out", 'w+') as fout:
                for line in file :
                    if (line.find(".text") != -1 or line.find("Aggreg") != -1) : pass
                    else :
                        fout.write(line.replace(": ", ", "))
            
        # fileContent = fileContent.replace(": ", ",")
        
        # with open(fileName, 'w') as file:
        #     file.write(fileContent)

def testParse() :
    os.chdir ("DataResults")
    with open("arm_bzip_00.txt", 'r', encoding="utf-16") as file:
            with open("arm_bzip_00.txt" + "_out", 'w+') as fout:
                for line in file :
                    if (line.find(".text") != -1 or 
                        line.find("Aggreg") != -1 or 
                        line.find("Found") != -1) : pass
                    else :
                        fout.write(line.replace(": ", ", "))
    pass

def main() :
    testParse()
    pass

if __name__ == "__main__" :
    main()