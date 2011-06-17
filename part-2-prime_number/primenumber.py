'''
Created on Jun 17, 2011

@author: xtephan
'''
import pyopencl as cl
import numpy


class PrimeCPU():
    '''
    Generates the first N prime numbers
    '''


    def __init__(self,limit):
        '''
        Constructor
        '''
        self.limit=limit
        self.primes=[]
        
    def compute(self):
        
       
        for nr in range(3,self.limit,+2):
            
            ok=1
            
            for div in range(2,nr/2):
                if (nr%div)==0:   #it's not prime
                    ok=0
                    break
            if ok:
                self.primes.append(nr)
            
    def display(self):
        
        for thisPrime in self.primes:
            print str(thisPrime)
            
#--------------------------------------------------------------------------------            
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

class PrimeGPU():
    '''
    Generates the first N prime numbers
    '''


    def __init__(self,limit):
        '''
        Constructor
        '''
        self.limit=limit
        
        self.ctx = cl.create_some_context()
        self.queue = cl.CommandQueue(self.ctx)
        
    def compute(self):
        
        #read openCL
        f = open("part2.cl", 'r')
        fstr = "".join(f.readlines())
        
        #create the program
        self.program = cl.Program(self.ctx, fstr).build()
        
        
        #popCorn
        mf = cl.mem_flags

        #initialize client side (CPU) arrays
        self.primes = numpy.array(range(self.limit), dtype=numpy.float32)

        #create OpenCL buffers
        self.dest_buf = cl.Buffer(self.ctx, mf.WRITE_ONLY, self.primes.nbytes)
        
        
        #execute
        self.program.part1(self.queue, self.primes.shape, None, self.dest_buf)

        #get the result
        cl.enqueue_read_buffer(self.queue, self.dest_buf, self.primes).wait()
        

            
    def display(self):
        

        for thisPrime in self.primes:
            print str(thisPrime)