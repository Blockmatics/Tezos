import smartpy as sp
class SimpleOperations(sp.Contract):
    def __init__(self):
        self.init(storedValue = 4, flag = True, deck = [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        
    @sp.entryPoint
    def set(self, params):
        self.data.storedValue = params.op
     
    @sp.entryPoint       
    def double(self, params):
        self.data.storedValue *= 2
        
    @sp.entryPoint       
    def divide(self, params):
        sp.verify(params.op > 0)
        self.data.storedValue /= params.op
        
    @sp.entryPoint       
    def factorial(self, params):
        self.data.storedValue = 1
        sp.for x in sp.range(1, params.op+1):
            self.data.storedValue *= x
            
    @sp.entryPoint       
    def reverseFlag(self, params):
        self.data.flag = ~self.data.flag
        
# Defines the contract test.
@addTest(name = "Test simple operations")
def testSimpleOperations():
   # Instantiates the contract.
   myContract = SimpleOperations()
   
   # Declares a string variable, to build a html output.
   html = myContract.fullHtml()

   # Calls the contract set method and converts output to html.
   html += myContract.set(op = 9).html()
   html += myContract.set(op = 17).html()

   html += myContract.divide(op = 6).html()
   html += myContract.factorial(op = 11).html()
   html += myContract.reverseFlag().html()

   
   # Outputs to screen.
   setOutput(html)
