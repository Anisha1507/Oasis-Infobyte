import random
import string
print("Welcome to the random password generator:")
length=int(input("Enter the length of the password: "))
print("Press 1 Password of letters\n2 Password of digits\n3 Password of symbols\n4 Password of alphanumeric and symbol")
choice=int(input("Enter Your choice:"))
def password_type(choice):
    match choice:
        case 1:
            chars=string.ascii_letters
            password=''.join([random.choice(chars) for i in range(length)])
            return password
        case 2:
            chars=string.digits
            password=''.join([random.choice(chars) for i in range(length)])
            return password
        case 3:
            chars=string.punctuation
            password=''.join([random.choice(chars) for i in range(length)])
            return password
        case 4:
            chars=string.ascii_letters
            chars+=string.digits
            chars+=string.punctuation
            password=''.join([random.choice(chars) for i in range(length)])
            return password
        case default:
            return "Wrong choice"
        
head=password_type(choice)
print("Your password is: ",head)
