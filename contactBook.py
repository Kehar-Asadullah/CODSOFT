

contacts={}
def add_c():
    name=input("Enter name of the contact ")
    num=int(input("Enter the contact number "))
    contacts[name]=num

def del_c():
    view_c()
    name=input("Which contact to delete? ")
    if name in contacts:
        deleted=contacts.pop(name)
        print(f"{name}    {deleted} is deleted")
    else:
        print("Contact does not exist")

def search_c():
    name=input("Enter the name of contact ")
    if name in contacts:
        print(f"{name}  {contacts[name]}")
    else: 
        print("Contact does not exist")

def view_c():
    if not contacts:
        print("No contact exist!")
    else:
        print("Name    Phone No.")
        for x in contacts:
            print(f"{x}   {contacts.get(x)}")
    
while True:
    print("\nCONTACT BOOK")
    print("**************")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. View contacts")
    print("5. Exit")
    ch=int(input("Enter the option number "))
    if ch==1:
        add_c()
    elif ch==2:
        del_c()
    elif ch==3:
        search_c()
    elif ch==4:
        view_c()
    else:
        break

print("End of the program")