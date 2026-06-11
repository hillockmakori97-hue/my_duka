from datetime import datetime
class Bank_account:
    def __init__(self,account_no,balance,owner_name,date_opened):
        self.balance=balance
        self.account_no=account_no
        self.owner_name=owner_name
        self.date_opened=date_opened

    def check_balance(self):
        print(f'you have a balance of Ksh {self.balance}')
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            res='withdrawal successful'
        else:
            res='balance too low, deposit and try again'
        return res
    def check_details(self):
        print(f''' 
        user_details 
        owner_name={self.owner_name}
        account_number={self.account_no}
        Account opened on {self.date_opened}
        ''')
    def close_account(self,account):
        print(f'account {account.account_no} was successfuly deleted')
        del account
acc1=Bank_account('ac1',40000,'john','12/4/2021')
acc1.withdraw(14000)
print(acc1.balance) 
acc1.check_balance()
acc1.close_account(acc1)
acc2=Bank_account('ac2',78000,'sydney','4/11/2025')
acc2.check_details()


