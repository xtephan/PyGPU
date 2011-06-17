'''
CopyLeft Stefan Fodor @ 2011
Created on Jun 17, 2011
'''

from primenumber import Prime
import datetime
from time import time

N_LIMIT=100000

if __name__ == "__main__":
    
    
    #----CPU--------------------------------------
    time1 = time()
    
    cpu=Prime(N_LIMIT)
    cpu.compute()
    cpu.display()
    
    time2 = time()
    print "Execution time of test without OpenCL: " + str(time2 - time1) + " seconds"