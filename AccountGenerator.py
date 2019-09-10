import string
import random

#loop asking how many characters user wants the password to be
while True:
    try:
        password = int(input("How many characters do you want your password to be?"))
        if password < 5:
            print("Password needs to be bigger than 5 characters,", password, "is too short, try again...")
            continue
    except ValueError:
        print("The input was incorrect, try again.")
        continue
    else:
        break

#loop asking for prefix of email
while True:
    try:
        lengthPrefix = int(input("How many characters do you the prefix of your email to be (between 5 and 25)?"))
        if lengthPrefix < 5 or lengthPrefix > 25:
            print("The given prefix length is not possible, try again...")
            continue
    except ValueError:
        print("The input was incorrect, try again.")
        continue
    else:
        break

#Loop asking for number of accounts user wants
while True:
    try:
        numberAccounts = int(input("How many accounts do you want to get?"))
        if numberAccounts < 1:
            print("The number of accounts cannot be a negative number! Try again...")
            continue
    except ValueError:
        print("The given value is incorrect, try again...")
        continue
    else:
        print("Thanks, that was all the needed input.")
        break

#Email generator function
def emailPrefix():
    prefix = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.sample(prefix, lengthPrefix))

#Password generator function
def randomPassword(length):
    password = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.sample(password, length))

#Arrays for domain names and hotmails
email = ["hotmail", "gmail", "live", "yahoo"]
domain = [".com", ".nl", ".pt", ".de", ".fr"]

#Printing the accounts
print("\nHere are some random accounts:")
for i in range(0, numberAccounts):
    print("Account", (1 + i), ":")
    print("Email:", emailPrefix() + "@" + random.choice(email) + random.choice(domain))
    print("Password:", randomPassword(password), "\n")