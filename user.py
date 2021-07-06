class user:
    def __init__(self, name):
        self.name = name
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount

    def balance(self):
        print(self.name)
        print(self.accountBalance)

    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount
        otherUser.accountBalance += amount


logan = user("logan")
jacob = user("jacob")
william = user("william")

logan.makeDeposit(200)
logan.makeDeposit(50)
logan.makeDeposit(1000)
logan.makeWithdrawal(350)
print(logan.accountBalance)

jacob.makeDeposit(7)
jacob.makeDeposit(3)
jacob.makeWithdrawal(5)
jacob.makeWithdrawal(4)
print(jacob.accountBalance)

william.makeDeposit(1000)
william.makeWithdrawal(250)
william.makeWithdrawal(450)
william.makeWithdrawal(50)
print(william.accountBalance)

logan.transferMoney(william, 300)
print(logan.accountBalance)
print(william.accountBalance)
