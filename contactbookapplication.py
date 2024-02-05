import json #using the json module means we have to import it
#the load_contacts function is used to open and read any existing contacts and it puts them into a contacts list, returning it to us
contacts = []
def load_contacts():
    try:
        with open("contacts.json", "r") as file:#opens the contacts.json file in reading mode(r), it names it as file, like we did with project one. The with statement ensures the file is properly handles
          contacts= json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts
#after saving we need to load our contacts to make sure they are not lost in memory
def save_contacts():
    with open("contacts.json", "w") as file:#in the case we are opening our file in write mode w, ensuring we save latest version of file if it already exists The with like usual just ensures proper handling
        json.dump(contacts, file)#so the json.dump functions takes the dataa(in this case the first argument: contacts) and then conversts it first to a string in JsSON-format then converts it into a file called file since its our second argument)
        
def display_menu():#this function gives the user all available actions
    print("\nCommand Line Contact Book")#prints new blank line then the title of our command line
    print("1. Show Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Exit")

def show_contacts(contacts):#takes contacts as an argument
    print("\nContacts:")    
    if not contacts:#check if the contacts list is empty. If so it returns true. Its just like cgecking if contacts is an empty list
        print("No contacts found")
    else:
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")#for each contact we print out the name and the phone. It is a dictionary so we extract information like dictionaryname[key name]. f and {} are present so we put answer directly into string
        
def add_contact():#contacts is a list of dictionaries, not a dictionary itself
    name_to_add = input("Enter contact name: ")
    phone_to_add = int(input("Enter contact number: "))
    new_contact = {"name": name_to_add, "phone": phone_to_add}#essentially what we do is make dictionary and add to the list  
    contacts.append(new_contact)
    save_contacts()#dont forget to save our contacts again

def search_contact(contacts):
    name_to_search = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        print(f"{contact['name']}, {contact['phone']}")#new formatting for each thing. each contact is dict not contacts
        found = True
        break
    if not found:#checks if found is still false, if so it prints 
        print("Name not found")
        
def main(): #main part of the program, we can call other functions from here
    while True:
        display_menu()
        choice = input("Enter your choice 1-4: ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            print("Exiting Contact Book. Goodbye! ")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4")

if __name__ == "__main__":
    main()
            

#dont forget the f so you can directly replace value. put print outside if you dont want multiple name not found        
