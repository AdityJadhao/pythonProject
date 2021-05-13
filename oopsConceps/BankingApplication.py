# write a program to create a banking application in which user can deposite a money,withdraw a money and check balance

# baseclass
import sys
class bankApp:
    bank = "AmraSBI"

    def __init__(self, name,balance=0):
        self.name = name
        self.balance = balance

    def deposite(self, amt):
       self.balance = self.balance+amt
       print("You have deposited Rs.:", self.balance)

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient Balance")
        elif amt < 0:
            print('Please enter valid amount')
        else:
            self.balance = self.balance - amt
            print("you have withdraw Rs:",amt)
        print('Your balance after transaction is:',self.balance)

#drived class
userName = input("Please enter your name:")
b = bankApp(userName)
print('Welcome to',bankApp.bank+" ,"+userName)
while True:
    print('D - deposit\nW-Withdraw\nE-Exit')
    option = input('Enter your option')
    if option=='d' or option=='D':
        amt = float(input('Enter amount to be deposited:'))
        b.deposite(amt)
    elif option=='w' or option=='W':
        amt = float(input('Enter amount to be withdraw:'))
        b.withdraw(amt)
    elif option=='e' or option=='E':
        print('Thank you for banking with us,Have a nice day')
        sys.exit()
    else:
        print('You have enter wrong option,Please select valid option')


