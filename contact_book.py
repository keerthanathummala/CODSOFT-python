def add_contact():
    x=open("contact_storage.txt","a")
    contact=input("\n\tContact : ")
    name=input("\tName : ").upper()
    address=input("\tAddress : ").replace("," , " , ")
    email=input("\tEmail : ").upper()

    x.write(f"{name},{contact},{email},{address}\n")
    x.close()
#asking if the user wants to return to homepage or not
    z= input("\t\tback to main page yes/no : ").lower() 
    if (z == "yes") or (z == "y"):
        main()
    elif (z == "no") or (z == "no"):
        pass

def delete_contact():
    pass
def update_contact():
    contact_name = input("Enter the name of the contact to update: ").upper()
    found = False

    with open("contact_storage.txt", "a") as x:
        for line in x:
            name, contact, email, address = line.strip().split(',')
            if name == contact_name:
                found = True
                contact = input("Enter new contact: ")
                email = input("Enter new email: ").upper()
                address = input("Enter new address: ").replace(",", " , ")
                # Write the updated contact details back to the file
                x.write(f"{name},{contact},{email},{address}\n")
                break
            
    if found:
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
    x.close()

    z= input("\t\tback to main page yes/no : ").lower() 
    if (z == "yes") or (z == "y"):
        main()
    elif (z == "no") or (z == "no"):
        pass

def view_contacts():
    x=open("contact_storage.txt", "r")
    for line in x:
        name, contact, email, address = line.strip().split(',')
        print(f"\n\tName: {name}\n\tContact: {contact}\n\tEmail: {email}\n\tAddress: {address}")
    x.close()
#asking if the user wants to return to homepage or not
    z= input("\t\tback to main page yes/no : ").lower() 
    if (z == "yes") or (z == "y"):
        main()
    elif (z == "no") or (z == "no"):
        pass

def search_contact():
    contact_name = input("Enter contact name to search: ").upper()
    found = False
    x=open("contact_storage.txt", "r")
    for line in x:
        name, contact, email, address = line.strip().split(',')
        if name == contact_name:
            print(f"\n\tName: {name}\n\tContact: {contact}\n\tEmail: {email}\n\tAddress: {address}")
            found = True
            break
    if not found:
        print("Contact not found.")
    x.close()
#asking if the user wants to return to homepage or not
    z= input("\t\tback to main page yes/no : ").lower() 
    if (z == "yes") or (z == "y"):
        main()
    elif (z == "no") or (z == "no"):
        pass
    
def main():
    print("\t\tCONTACTS ")
    print("\n1. add new contact \n2. delete contact \n3. update contact \n4. view contact information \n5. search contact")
    select=input("\nplease select the number you want to proceed with : ")
    if select == "1":
        add_contact()
    elif select == "3":
        update_contact()
    elif select == "4":
        view_contacts()
    elif select == "5":
        search_contact()
    else:
        print("\nplease select from option from above \n")
        main()

if __name__== "__main__":
    main()
