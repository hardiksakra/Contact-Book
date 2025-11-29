import csv
import os
CONTACT_BOOK = "Contack Book"
os.makedirs(CONTACT_BOOK , exist_ok=True)

def add_contack():
   
   name = input("Enter Full Name : ").lower()
   
   contact_number = int(input("Enter Contact Number"))

   file_path = os.path.join(CONTACT_BOOK , f"{name}.csv")

   with open(file_path, "w" , newline="") as file:
       print("Adding Contact...")
       writer = csv.writer(file)
       writer.writerow(["Name" , "Contact Number"])
       writer.writerow([name , contact_number])
       print(f"✅ Contact '{name}' added successfully!\n")


def view_All():
    files =os.listdir(CONTACT_BOOK)

    for f in files:
        contack_path = os.path.join(CONTACT_BOOK ,f)
        
        with open(contack_path) as read:
            reader = csv.reader(read)
            next(reader)
            for row in reader:
                print(f"👤 {row[0]} — 📞 {row[1]}")
        print()

def search_contact(search_file):
    
    files_search_path = os.listdir(CONTACT_BOOK)
    found = False
    for f in files_search_path:
        contact_path = os.path.join(CONTACT_BOOK , f)

        with open(contact_path) as read:
            reader = csv.reader(read)
            next(reader)
            for row in reader:
                if(row[0] == search_file):
                    print(f"Found contact : 👤 {row[0]} — 📞 {row[1]}")
                    break
    if(found == False):
        print("👤Contact Not Founded")

    print()        

    
def delete_contact():
     delete_name = input("Enter Name : ").lower()
     files =os.listdir(CONTACT_BOOK)
     for file_name in files:
         if(file_name == delete_name + ".csv"):
            file_path = os.path.join(CONTACT_BOOK, file_name)
            os.remove(file_path)
            print(f"✅ Contact '{delete_name}' deleted successfully!")
            break
         else:
             print("Not Found")

       
def main():

    print("..........📒 CONTACT BOOK............\n")
    while True:
        print("📒 CONTACT BOOK")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        try:
            choice = int(input("Enter your Choice : "))

            match choice:
                case 1:
                   add_contack()
                case 2:
                    view_All()

                case 3:
                    search_file = input("Enter name to be seareched : ").lower()
                    search_contact(search_file)

                case 4:
                  
                  delete_contact()
                    
                case 5:
                    print("Thank You!")
                    break


        except Exception as e:
            print(".............Enter Valid Input.............. \n")
            return main()







if __name__ == "__main__":
    main()