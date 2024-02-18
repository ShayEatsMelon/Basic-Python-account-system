class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

#asks for the name and pin
name = (input("Enter your name for the new account:\n"))
pin = (input("Enter your pin for the new account:\n"))

#checks if the name is actually a name and if the pin is actually a pin
if not name.isalpha():
    print("Sorry, the name can only contain alphabetic characters.")
    exit()
    
#checks if the name and pin are big enough
if len(name) <= 3 or len(pin) <= 5:
    print("Sorry, the name must be more than 3 letters and the pin must be more than 5 numbers.")
    exit()

try:
    pin = int(pin)
except ValueError:
    print("Invalid pin. Please enter a valid pin next time.")
    exit()

#confirmation of account details
confirm_name = input("What is the name of your account?")
confirm_pin = input("What is the pin of your account?")

#checks if the confirmations are numbers and letters
if not confirm_name.isalpha():
    print("Sorry, the name can only contain alphabetic characters.")
    exit()
    
try:
    confirm_pin = int(confirm_pin)
except ValueError:
    print("Invalid pin. Please enter a valid pin next time.")
    exit()

#actually check to see if the confirmations are correct
if confirm_name == account.name and confirm_pin == account.pin:
    print("Correct. You are now logged in.")
else:
    print("Incorrect. Your name or pin is wrong.")
    exit()