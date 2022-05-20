class Atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number
    def check_balance(self):
        print("your balance is 9000$") 
    def withdraw(self,amount):
        new_amount=9000-amount
        print("you have withdrawn"+str(amount)+". your remaining balance is"+str(new_amount))
def main():
    card_number=input("insert your card number: ")
    pin_number=input("enter your pin number: ")
    new_user=Atm(card_number,pin_number)
    print("choose your activity")
    print("1.balance Enquiry  2.withdrawal")  
    activity=int(input("enter activity number: "))
    if activity==1:
        new_user.check_balance()
    elif activity==2:
        amount=int(input("enter the amount: "))
        new_user.withdraw(amount)
    else:
        print("enter the valid numeber")
if __name__=="__main__":
    main()                

