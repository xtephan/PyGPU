'''
Created on Jun 17, 2011

@author: xtephan
'''

class Prime():
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