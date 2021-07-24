class FibIterator():
    def __init__(self, initCounter):
        self.counter = initCounter

    def __next__(self):
        self.counter+=1
        return self.fib(self.counter)

    def fib(self,n,memoVar=None):
        '''
        time complexity : O(n)
        space complexity : O(n)
        '''
        if not isinstance(n,int) or n<1:
            return -1 #handles invalid values
        if memoVar is None:
            memoVar=dict()
        if n in memoVar:
            return memoVar[n]
        if n<=2:
            return 1 #base condition to return 
        memoVar[n]=self.fib(n-1,memoVar)+self.fib(n-2,memoVar)
        return memoVar[n]   

if __name__=="__main__":
    iterator = FibIterator(3)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))