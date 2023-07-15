from tabulate import tabulate
from prettytable import PrettyTable
import json
import pandas as pd
import re

address_book = {}


class addressBookAssignment():   

# Creating address book 

    def address_details(self):
        
        
        adress_book_count = int(input('enter the number of address books : '))
        #prev_book = []  
        #book_name = ' '
        
        while adress_book_count > 0:
            
            book_name = input("enter  adress book name : ")
            
            
            if book_name not in address_book.keys(): 
                
                address_book[book_name] = {}      
                #prev_book.append(book_name)

                #first_name = input('Enter first name: ')
                first_name = self.regex_fname_validation()
                address_book[book_name]['First Name'] = first_name
                
                last_name = self.regex_lname_validation()
                address_book[book_name]['Last Name'] = last_name
                
                address = input('Enter address: ')
                address_book[book_name]['Address'] = address
                
                city = input('Enter city name: ')
                address_book[book_name]['City'] = city
                
                state = input('Enter state name: ')
                address_book[book_name]['State'] = state

                zip_code = self.regex_zipcode_validation()
                address_book[book_name]['Zip Code'] = zip_code
                
                mobile = self.regex_mobile_validation()
                address_book[book_name]['Mobile'] = mobile

                email = self.regex_email_validation()
                address_book[book_name]['Email'] = email

                adress_book_count -= 1

                

            else:
                print("Already exists")
                adress_book_count = adress_book_count

        
            #t= PrettyTable(['Name', 'Last name', 'Address', 'City', 'State', 'Zipcode', 'Mobile'])
        
            #t.add_row([first_name, last_name, address, city, state, zip_code, mobile])
            #print(t)

                    #abc = address_book(my_address_book)
                
        return address_book
        
    
    #details = address_details()
    #print(details)


# Editing address book details

    def edit_addressbook(self):
        # (options for editing) - based on adress book name edit the person details
        # all details -

        print('Edit details\n1:Mobile No\n2:Email Address\n3:Address\n4:All details ')
        choice = int(input())
            

        book_name = " "
        while book_name not in address_book.keys():

                book_name = input('Select the address book name : ')
                if book_name not in address_book.keys():
                    print('Address book is not there, enter the valid name')
                    continue
                else:
                    
                    if int(choice) == 1:
                        mobile = self.regex_mobile_validation()
                        address_book[book_name]['Mobile'] = mobile

                    elif int(choice) == 2:
                        email = self.regex_email_validation()
                        address_book[book_name]['Email'] = email

                    elif int(choice) == 3:
                        address = input('Enter address you want to edit: ')
                        address_book[book_name]['Address']  = address

                    elif int(choice) == 4:
                        all_edit = input("You want to edit all details [Y/N] : ")
                        if all_edit.upper() == 'Y':
                            first_name = self.regex_fname_validation
                            address_book[book_name]['First Name'] = first_name
                            
                            last_name = self.regex_lname_validation
                            address_book[book_name]['Last Name'] = last_name
                            
                            address = input('Enter address: ')
                            address_book[book_name]['Address'] = address
                            
                            city = input('Enter city name: ')
                            address_book[book_name]['City'] = city
                            
                            state = input('Enter state name: ')
                            address_book[book_name]['State'] = state

                            zip_code = self.regex_zipcode_validation
                            address_book[book_name]['Zip Code'] = zip_code
                            
                            mobile = self.regex_mobile_validation
                            address_book[book_name]['Mobile'] = mobile  

                            email = self.regex_email_validation()
                            address_book[book_name]['Email'] = email  

                        else:
                            print('No update needed')  
                

        return address_book   

                

    #edit_details = edit_addressbook()
    #print(edit_details)


# address book delete

    def delete_addressbook(self):
        Book = address_book.keys()
        print(f'The existing address books are : {Book}')
        book_name = input('Enter the address book name that you want to delete : ')
        print(address_book) 
        del address_book[book_name]
        return address_book
        

    #delete_addressbook()

# write adressbook in json
    def write_json(self):
        json_obj = json.dumps(address_book, indent=4)
        with open("D:\\FirstTest\\PythonSelenium\\address_book.json", "w") as output:
            #json.dump(address_book, output)
            output.write(json_obj)
        
    #write_json()    


#read from json
    def read_json(self):
        with open("D:\\FirstTest\\PythonSelenium\\address_book.json", "r", encoding ='utf-8') as output:
            jsonobj = json.load(output)
        print(jsonobj)

    #read_json()



# display address book
    def display_addressbook(self):
        print(address_book)

        display_df = pd.DataFrame(address_book)
        print(display_df)

# Regex validation

    def regex_fname_validation(self):
        
        while True:
            first_name = input('Enter first name: ')
            if re.match("^[A-Z]{1}[A-Z-a-z]*$", first_name):
                break
                
            else:
                print("Oopss..!! Enter valid first name")
                continue

    def regex_lname_validation(self):
        
        while True:
            last_name = input('Enter last name: ')
            if re.match("^[A-Z]{1}[A-Z-a-z]*$", last_name):
                break
                
            else:
                print("Oops..!! Enter valid last name")
                continue

    def regex_mobile_validation(self):
        
        while True:
            mobile = input('Enter mobile number: ')
            if re.match("^(91){1}[0-9]{10}", mobile):
                break
                
            else:
                print("Ooopss..!! Enter valid mobile number")
                continue   
        return mobile     

    def regex_email_validation(self):
        while True:
            email = input('Enter email address: ') 
            if re.match("^[A-Za-z0-9]*(@gmail.com)$", email) or re.match("^[A-Za-z0-9]*(@yahoo.com)$", email) :
                break
            else:
                print("Ooops..!! Enter valid email address")
                continue
        return email
    
    def regex_zipcode_validation(self):
        while True:
            zip_code = input('Enter zip_code: ')
            if re.match("^[0-9]{6}$", zip_code):
                break
            else:
                print("Oopss..!! Enter valid Zipcode : ")

        return zip_code







#display_addressbook()

if __name__ == "__main__":
    print('welcome to address book')

    adress_book_obj = addressBookAssignment()
   
    while True:

        print('1:Create address book\n2:Edit address book\n3:Display address book\n4:Delete address book\n5:Write to JSON\n6:Read JSON\n7:Exit the process')

        option = int(input())
        if option == 1:
            adress_book_obj.address_details()

        elif option == 2:
            adress_book_obj.edit_addressbook()
        
        elif option == 3:
            adress_book_obj.display_addressbook()

        elif option == 4:
            adress_book_obj.delete_addressbook()

        elif option == 5:
            adress_book_obj.write_json()

        elif option == 6:
            adress_book_obj.read_json()

        elif option == 7:
            break







    # t= PrettyTable(['Name', 'Last name', 'Address', 'City', 'State', 'Zipcode', 'Mobile'])
    
    # t.add_row([fname, lname, address, city, state, zipcode, mobile])
    # print(t)

    

#address_book(ufname,ulname,uaddress,ucity,ustate,uzipcode,umobile)



# regex = fname and lname validation, fname - min 3 letter, first letter capital
#mail : should be @yahoo gmail, else re-enter
#phone number 91, should be 10 digits
# it should b int and 6 digit 