class bank():
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def deposit(self,credit_balance):
        if int(credit_balance) <= 0 :
            return "Credited Invalid amount"
        else:
            self.balance += int(credit_balance)
            return self.balance
    
    def withdrawl(self,debit_balance):
        if int(debit_balance) > self.balance:
            return "Draw exceeds available balance"
        else:
            self.balance -= int(debit_balance)
            return self.balance
owner_name = input("Enter owner name: ")
amount = int(input("Enter amount: "))
owner = bank(owner_name,amount)
while(True):
    own = input().split(" ")
    if (own[0] == 'withdrawl'):
        print(owner.withdrawl(own[1]))
    elif (own[0] == 'deposit'):
        print(owner.deposit(own[1]))
    else:
        break
    
