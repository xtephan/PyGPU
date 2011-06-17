'''
CopyLeft Stefan Fodor @ 2011
Created on Jun 17, 2011
'''

from primenumber import PrimeCPU
from primenumber import PrimeGPU
from timeit import Timer

N_LIMIT=1000000

def doCPU():
    cpu=PrimeCPU(N_LIMIT)
    cpu.compute()

def doGPU():
    gpu=PrimeGPU(N_LIMIT)
    gpu.compute()
    #gpu.display()

if __name__ == "__main__":
    

    #----------------CPU--------------------------------------
    t = Timer("doCPU()","from __main__ import doCPU")
    print "Execution time of test without OpenCL: " + str(t.timeit(number=1)) + " seconds"

    
    #----------------GPU--------------------------------------
    t2 = Timer("doGPU()","from __main__ import doGPU")
    print "Execution time of test with OpenCL: " + str(t2.timeit(number=1)) + " seconds"
    