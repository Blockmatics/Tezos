import smartpy as sp

class SimpleOperations(sp.Contract):
    def __init__(self):
        self.init(storedValue = 4, flag = True, deck = [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        
    @sp.entry_point
    def set(self, params):
        self.data.storedValue = params.op
     
    @sp.entry_point       
    def double(self, params):
        self.data.storedValue *= 2
        
    @sp.entry_point       
    def divide(self, params):
        sp.verify(params.op > 0)
        self.data.storedValue /= params.op
        
    @sp.entry_point       
    def factorial(self, params):
        self.data.storedValue = 1
        sp.for x in sp.range(1, params.op+1):
            self.data.storedValue *= x
            
    @sp.entry_point       
    def reverseFlag(self, params):
        self.data.flag = ~self.data.flag
        
# Defines the contract test.
@sp.add_test(name = "Test simple operations")
def testSimpleOperations():
   # Instantiates the contract.
   myContract = SimpleOperations()

   scenario = sp.test_scenario()
   scenario += myContract

   scenario += myContract.set(op = 9)
   scenario += myContract.set(op = 17)

   scenario += myContract.divide(op = 6)
   scenario += myContract.factorial(op = 11)
   scenario += myContract.reverseFlag()
