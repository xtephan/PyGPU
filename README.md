PyGPU
----

Playing with GPU and python. 

My working environment
---
* Ubuntu 11.04
* ATI 5470 graphic

Install
---

1. Install the ATI driver under Linux. 

2. Install OpenCL dependencies
```sh
$ apt-get install freeglut3-dev python-numpy
```

3. Install OpenCL, packages amd-app-2.4 and amd-app-dev. 
(last known link is http://forums.amd.com/forum/messageview.cfm?catid=390&threadid=125792&STARTPAGE=1&FTVAR_FORUMVIEWTMP=Linear)

4. Do a dryrun of OpenCL
```sh
$ cat "#include <CL/opencl.h>" > testcl.c
$ gcc testcl.c -o prog -lOpenCL
```
5. Download pyopencl.
(last known link http://pypi.python.org/pypi/pyopencl)

6. Unpack and install
```sh
$ python setup.py build
$ python setup.py install 
```

Structure
---

####Part 1#####
Contains a code that sums 2 vectors using GPU.

####Part 2#####
Finds the prime numbers until N. 

(I know there are better algorithms than the one I have implemented, but the porpuse is to test the GPU.)

Benchmarks
---

####Vector Sum#####
Execution time of test without OpenCL: 11.731222868 seconds

Execution time of test with OpenCL: 0.521452188492 seconds

####Prime numbers#####
N=100

Execution time of test without OpenCL: 0.000123023986816 seconds

Execution time of test with OpenCL: 0.601119995117 seconds

N=1000

Execution time of test without OpenCL: 0.00573706626892 seconds

Execution time of test with OpenCL: 0.579922914505 seconds

N=10000

Execution time of test without OpenCL: 42.7467110157 seconds

Execution time of test with OpenCL: 5.0943210125 seconds

Notes
---

This code has not been updates since 2013 and it is less likely that will be again.

License
---
Copyright Stefan Fodor @ 2013

This program is free under the terms of GNU GPL licence.

Feel free to copy, modify and redistribute.
