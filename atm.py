class ATM(object):
    def __init__(self,card,pin):
       self.card=card
       self.pin=pin
    def withdrawl(self):
        n=input("how much would you like to take out\n")
        print("you have succesfully withdrawl rupees",n)
    
    def pin(self):
        print("enter your card number")

    def deposit(self):
        print("enter the value you would like to deposit!")
        

    
      

QB=ATM("withdrawl","deposit")
QB.withdrawl()   
print(QB.card)

  