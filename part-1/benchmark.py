'''
CopyLeft Stefan Fodor @ 2011
Created on Jun 17, 2011

Based on an example provided by Roger Pau Monn'e
'''

import pyopencl as cl
from main import CL
import numpy
import numpy.linalg as la
import datetime
from time import time

a = numpy.random.rand(1000).astype(numpy.float32)
b = numpy.random.rand(1000).astype(numpy.float32)
c_result = numpy.empty_like(a)

# Speed in normal CPU usage
time1 = time()
for i in range(1000):
        for j in range(1000):
                c_result[i] = a[i] + b[i]
                c_result[i] = c_result[i] * (a[i] + b[i])
                c_result[i] = c_result[i] * (a[i] / 2.0)
time2 = time()
print "Execution time of test without OpenCL: " + str(time2 - time1) + " seconds"


# GPU power
time3 = time()
example = CL()
example.loadProgram("part1.cl")
example.popCorn(1000)
example.execute()
time4 = time()

print "Execution time of test with OpenCL: " + str(time4 - time3) + " seconds"
