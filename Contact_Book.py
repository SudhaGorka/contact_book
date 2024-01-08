#Contact Book:
#Create a simple contact book where users can add, view, update, and delete contacts. Each contact can have attributes like name, phone number, and email stored in a dictionary.
Dict = {}

def add_contact(Dict,name,phone_number,email):
    if name not in Dict:
        Dict[name]=phone_number,email
        print("Contact Details of",name,"is added successfully")
    else:
        print([name],"is already present in the Contact Book")

def view_dict(Dict,name):
    print(Dict)

def update_contact(Dict,name,phone_number2,email2):
    if name not in Dict:
        Dict[name]=phone_number2,email2
        print([name],"is successfully updated!")
    else:
         Dict[name]=phone_number2,email2
         print([name],"is successfully updated")

def del_contact(Dict,name):
    del Dict[name]
    print([name],"is successfully deleted from Contact Book")


while True:
    print("MENU")
    print("1. Add Users in the Book")
    print("2. View Book ")
    print("3. Update contacts")
    print("4. Delete contact")
    print("5. Quit")

    n=int(input("Enter the no. : "))

    if n==1:
          name=input("Enter the name of user: ")    
          phone_number=input("Enter the phone number of the user: ")
          email=input("Enter the email of user: ")
          add_contact(Dict,name,phone_number,email)

    elif n==2:
        view_dict(Dict,name)
    elif n==3:
        name=input("Enter the name of user you want to update: ")
        phone_number2=input("Enter the phone no.: ")
        email2=input("Enter the email: ")
        update_contact(Dict,name,phone_number2,email2)
    elif n==4:
         name=input("Enter the name you want to delete: ")
         del_contact(Dict,name)
    elif n==5:
        print("You Successfully come out of the program!")
        break
    else:
        print("You entred wrong input!")

    
















    

    

        
