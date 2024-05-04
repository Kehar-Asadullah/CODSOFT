import string
import random

try:
    while True:
        length = int(input("Enter the length of the password: "))

        uCase= string.ascii_uppercase
        lCase= string.ascii_lowercase
        digits= string.digits
        symbols= string.punctuation

        mixed = uCase+lCase+digits+symbols
        password=random.sample(mixed, length)
        pwd="".join(password)
        print(f" '{length}' characters long password is '{pwd}' ")
        choice=input("\nDo you want to continue [y/n]: ").lower()
        if choice == 'y':
            continue
        else:
            print("End of the program!")
            break
except:
    print("Invalid input!")
finally:
    print("Bye Bye!!")
    