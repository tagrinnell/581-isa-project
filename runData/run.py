import subprocess
import time

for opt in ["O3", "O2", "O1", "O0"]:
    config = open("../../config/default.cfg", "r")
    data = config.read().splitlines(True)
    config.close()
    config = open("../../config/default.cfg", "w")
    for line in data:
        if line.startswith("COPTIMIZE"):
            line = f"COPTIMIZE   = -{opt} -fno-strict-aliasing\n"
        if line.startswith("CXXOPTIMIZE"):
            line = f"CXXOPTIMIZE = -{opt} -fno-strict-aliasing\n"
        if line.startswith("FOPTIMIZE"):
            line = f"FOPTIMIZE   = -{opt} -fno-strict-aliasing\n"
        config.write(line)
    config.close()
    print("Config Done " + opt)
    proc = subprocess.Popen("runspec -a build 401 --config default", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen("runspec -a build 403 --config default", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen(f"mv 401.bzip2/exe/bzip2_base.gcc43-64bit 401.bzip2/exe/bzip2_base_{opt}.gcc43-64bit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen(f"mv 403.gcc/exe/gcc_base.gcc43-64bit 403.gcc/exe/gcc_base_{opt}.gcc43-64bit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("X86 Bins Done " + opt)
    proc = subprocess.Popen("runspec -a build 401 --config arm", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen("runspec -a build 403 --config arm", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen(f"mv 401.bzip2/exe/bzip2_base.gcc43-32bit 401.bzip2/exe/bzip2_base_{opt}.gcc43-32bit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen(f"mv 403.gcc/exe/gcc_base.gcc43-32bit 403.gcc/exe/gcc_base_{opt}.gcc43-32bit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("ARM Bins Done " + opt)
    proc = subprocess.Popen(f"/home/vm-user/gem5/build/X86/gem5.opt -r -e -d /home/vm-user/finalprojruns/bzip2_X86{opt}_m5out /home/vm-user/gem5/configs/deprecated/example/se.py --cpu-clock=3GHz --mem-size=2GB --cpu-type=X86MinorCPU --caches --l2cache -I 100000000 --cmd /home/vm-user/SPEC/benchspec/CPU2006/401.bzip2/exe/bzip2_base_{opt}.gcc43-64bit --options \"/home/vm-user/SPEC/benchspec/CPU2006/401.bzip2/run/run_base_test_gcc43-64bit.0000/input.program 5\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("X86 bzip2 Done " + opt)
    proc = subprocess.Popen(f"/home/vm-user/gem5/build/X86/gem5.opt -r -e -d /home/vm-user/finalprojruns/gcc_X86{opt}_m5out /home/vm-user/gem5/configs/deprecated/example/se.py --cpu-clock=3GHz --mem-size=2GB --cpu-type=X86MinorCPU --caches --l2cache -I 100000000 --cmd /home/vm-user/SPEC/benchspec/CPU2006/403.gcc/exe/gcc_base_{opt}.gcc43-64bit --options /home/vm-user/SPEC/benchspec/CPU2006/403.gcc/run/run_base_test_gcc43-64bit.0000/cccp.in", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("X86 gcc Done " + opt)
    proc = subprocess.Popen(f"/home/vm-user/gem5/build/ARM/gem5.opt -r -e -d /home/vm-user/finalprojruns/bzip2_ARM{opt}_m5out /home/vm-user/gem5/configs/example/arm/starter_se.py --mem-size=2GB --cpu-freq=3GHz --cpu=minor -I 100000000 \"/home/vm-user/SPEC/benchspec/CPU2006/401.bzip2/exe/bzip2_base_{opt}.gcc43-32bit /home/vm-user/SPEC/benchspec/CPU2006/401.bzip2/run/run_base_test_gcc43-32bit.0000/input.program 5\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("ARM bzip2 Done " + opt)
    proc = subprocess.Popen(f"/home/vm-user/gem5/build/ARM/gem5.opt -r -e -d /home/vm-user/finalprojruns/gcc_ARM{opt}_m5out /home/vm-user/gem5/configs/example/arm/starter_se.py --mem-size=2GB --cpu-freq=3GHz --cpu=minor -I 100000000 \"/home/vm-user/SPEC/benchspec/CPU2006/403.gcc/exe/gcc_base_{opt}.gcc43-32bit /home/vm-user/SPEC/benchspec/CPU2006/403.gcc/run/run_base_test_gcc43-32bit.0000/cccp.in\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    print("ARM gcc Done " + opt)
