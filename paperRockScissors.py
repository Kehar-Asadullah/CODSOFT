

import random
name = input("\nEnter your name: ")
ls = ["paper","scissors", "rock"]
computer = random.choice(ls)
while True:
    user=input("Enter your option (paper, scissors and rock): ")
    if user in ls:
        print(f"'{name}' has selected {user} ")
        print(f"computer has selected {computer}")

        if user == computer:
            print("It's a tie!")
        elif user=="paper" and computer=="rock":
            print(f"'{name}' wins!")
        elif user=="rock" and computer=="scissors":
            print(f"'{name}' wins!")
        elif user=="scissors" and computer=="paper":
            print(f"'{name}' wins!")
        else:
            print(f"'{name} lost!")
    again=input("\nDo you want to continue [y/n] " ).lower()
    if again != 'y':
        break

print("End of Program")

