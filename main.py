#BANK_INFO
#Parent class
class User():
    #Hold details about user.
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Function to show user details.
    def Show_details(self):

        print("Personal Details:")
        print("")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)

#Child class
class Indian_Bank(User):
    #Store details about A/C balance
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    #Store details about deposite A/C balance
    def deposite(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("A/C balance has been updated:",self.balance)

    #Show withdraw amount and A/C balance
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance avaliable:",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("A/C balance has been updated:",self.balance)

    #View A/C balance
    def View_balance(self):
        self.Show_details()
        print("A/C balance:",self.balance)

details = Indian_Bank('ABC',20,'Male')
details.Show_details()
details.deposite(10000)
details.withdraw(500)
details.View_balance()

details = Indian_Bank('XYZ',40,'MALE')
details.Show_details()
details.deposite(50000)
details.withdraw(10000)
details.View_balance()