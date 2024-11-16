#importing json
import json
#importing tkinter as tk 
import tkinter as tk
#from tkinter importing ttk and message box
from tkinter import ttk
from tkinter import messagebox
#importing date and time
from datetime import datetime

#from the GUI.py file  importing the main class 
from GUI import FinanceTrackerGUI



transactions = {}  # Define transactions as a dictionary
#creating a json file
path = "Coursework2.json"

# File handling functions
def load_transactions():
    global transactions  # Use global keyword to modify the global transactions variable
    try:
        with open(path, "r") as f:
            transactions = json.load(f)  # Load transactions from the file
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty dictionary
        transactions = {}
#creating a function to save all the data into the json file
def save_transactions():
    with open(path, "w") as f:
        json.dump(transactions, f, indent = 4)  # Save transactions to the file

#creating a function to read bulk in a normal text file
def read_bulk_transactions_from_file(filename):
    
    global transactions
    try:
        with open(filename, 'r') as file:
            for line in file:#creating a loop
                line_parts = line.strip().split(',')
                if len(line_parts) == 3:
                    category, amount, date = line_parts#getting the order of the dictionary
                    category = category.capitalize()
                    try:
                        amount = float(amount)
                        # Check if the category already exists in transactions dictionary
                        if category in transactions:
                            transactions[category].append({"amount": amount, "date": date})
                        else:
                            # If the category doesn't exist, create a new one
                            transactions[category] = [{"amount": amount, "date": date}]
                    except ValueError:
                        print(f"Invalid amount '{amount}' in line: {line}")#printing the output
                else:
                    print("Invalid format in line:", line)
                    
        print("Bulk transactions added successfully.")
        save_transactions()  # Save the updated transactions to the file
    except FileNotFoundError:
        print(f"File '{filename}' not found.")#error handling

    
    pass


#Creating a function to add the transactions to the json file
def add_transaction():
    while True:#creating a loop
        transaction_name = input("\nEnter the name of the transaction which  you have made: ").capitalize()#getting the input
        while True:#creating a loop
            #error handling
            try:
                amount = float(input(f"\nEnter the {transaction_name} amount: "))  # Corrected conversion to float
                break#extitng from the loop
            except ValueError:
                print("\nInvalid amount entered. Please enter a valid number.")
                
        while True:# creating a loop
            #error handling
            try:
                date = input(f"\nEnter the date you made the above transaction ({transaction_name}) (YYYY-MM-DD): ")#getting the inputs
                datetime.strptime(date, "%Y-%m-%d")#importing the correct time 
                break#extitng from the loop
            except ValueError:
                print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.")

        
            
        
        transactions.setdefault(transaction_name, []).append({"amount": amount, "date": date})#appending the user inputs for the dictionary

        user_choice = input("\nDo you have to add another expense (Y/N): ").upper()#getting the user input
        if user_choice != "Y":
            break #extitng from the loop


    save_transactions()

                         
            
        
        
    
    pass

#creating a function to view all the transactions whic have been made so far
def view_transactions():
    if not transactions:#checking the trasactions 
        print("\nThere are no transactions")
    else:
        
        count = 1#setting a count
        for transaction_name, entries in transactions.items():#creating a loop
            print(f"\n{count}.Transaction: {transaction_name}")
            count+=1#increasing the count
            
            for entry in entries:#creating a loop
                print(f"\n Amount: {entry['amount']}, Date: {entry['date']}")#printing the outputs
                
                

    
    pass

#creating a function to update all the input values
def update_transactions():
    view_transactions()#calling the function
    
    while True:#creating a loop
        #error handling
        try:
            user_choice1 = input("\nEnter the name of the transaction you want to update: ").capitalize()#getting user inputs
            
            if user_choice1 in transactions:#checking the transactions
                print(f'\n{user_choice1} : {transactions[user_choice1]}')#printing the outputs
                break#extitng from the loop
            else:
                print("\nNo transaction found!")#printing the outputs
                continue#continuing the loop
                
        except ValueError:
            print("\nInvalid input for transaction name!")#printing the outputs
            continue#continuing the loop

    while True:#creating a loop
        #error handling
        try:
            #getting the user inputs
            update = input(f"\nEnter the category you want to update in {user_choice1} (Amount/Date) If you want to exit, please enter (Exit): ").capitalize()

            #checking the conditions
            if update == "Amount":
                while True:#creating a loop
                    #error handling
                    try:
                        index = int(input("\nEnter the number of the selected transaction list you want to update: "))
                        
                        if 0 <= index <= len(transactions[user_choice1]):#chacking the length
                            try:#error handling
                                amount1 = float(input(f"\nEnter the amount that you want to update in {user_choice1}: "))
                                transactions[user_choice1][index-1]['amount'] = amount1
                                print("\nThe amount is successfully updated!")#printing the outputs
                                break#extitng from the loop
                            except ValueError:
                                print("\nInvalid input. Enter a valid number.")#printing the outputs
                                continue#continuing the loop
                        else:
                            print("\nInvalid index. Please enter a valid index.")#printing the outputs
                            continue
                    except ValueError:
                        print("\nInvalid input. Enter a valid integer index.")#printing the outputs
                        continue#continuing the loop
                    
            elif update == "Date":#checking the conditions
                while True:#creating a loop
                    try:#error handling
                        index = int(input("\nEnter the number of the selected transaction list you want to update: "))
                        
                        if 0 <= index <= len(transactions[user_choice1]):#checking the length
                            try:#error handling
                                date1 = input("\nEnter the new date (YYYY-MM-DD): ")
                                datetime.strptime(date1, "%Y-%m-%d")
                                transactions[user_choice1][index-1]['date'] = date1
                                print("\nDate updated successfully!")#printing the outputs
                                break#extitng from the loop
                            except ValueError:
                                print("\nInvalid input. Enter the date in YYYY-MM-DD format.")#printing the outputs
                                continue#continuing the loop
                        else:
                            print("\nInvalid index. Please enter a valid index.")#printing the outputs
                            continue#continuing the loop
                    except ValueError:
                        print("\nInvalid input. Enter a valid integer index.")#printing the outputs
                        continue#continuing the loop
                        
            elif update == "Exit":
                break#extitng from the loop
                
            else:
                print("\nInvalid category. Please enter 'Amount', 'Date', or 'Exit'.")#printing the outputs
                continue#continuing the loop
                
        except ValueError:
            print("\nInvalid input for update!")#printing the outputs
            continue#continuing the loop

    save_transactions()#calling the function


 
    

    
    
    pass
#creating a function to delete the transactions
def delete_transactions():
    view_transactions()#calling the function
    #creating a loop
    while True:
    
        user_choice2 =input("\nEnter the transactions which you want to delete : ").capitalize()#getting the user inputs
        if user_choice2 in transactions:#cheking the conditions
            print(f'\n{user_choice2} : {transactions[user_choice2]}')#printing the outputs
            break#extitng from the loop
        else:
            print(f"\nInvalid input there is no trasaction called {user_choice2}")#printing the outputs

#creating a loop
    while True:
        index1 = 1
        index1 = int(input(f"\nEnter the number of the {user_choice2} list which you want to delete : "))#getting the user inputs
        if 1<=index1<=len(transactions[user_choice2]):#checking the conditions
            del transactions[user_choice2][index1-1]#deleting the selected transaction
            if len(transactions[user_choice2])<1:#checking the length of the transactions
                del(transactions[user_choice2])#deleting the selected transaction
            print("\nThe Selected item is deleted succssesfully !")#printing the outputs
            
            break#extitng from the loop
        else:
            print("\nInvalid input please try again")#printing the outputs



#calling the function
    save_transactions()
        
            
            
        

            
            
    

    
    pass

#creating a function to display the total
def display_summary():
    view_transactions()#calling the function
    total_expense = 0#creating local variable
    for transaction_name, entries in transactions.items():#creating a loop
        for entry in entries:#creating a loop
            total_expense += entry['amount']

    print(f'\nThe total of the expenses are : {total_expense}')#printing the outputs
    

    
    

    
    pass


#creating a main function to call all the functions at once
def main_menu():
    load_transactions()  # Load transactions at the start
    while True: #creating a loop till the value is true

        #printing the main out put of the code
        name = "Welcome to Personal Finance Tracker"
        print(name.center(50,'*'))
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Bulk Reading")
        print("7. Open the GUI for the Transactions")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        #Conditions
        
        if choice == '1':
            add_transaction()#calling the add function
        elif choice == '2':
            view_transactions()#calling the view function
        elif choice == '3':
            update_transactions()#calling the update function
        elif choice == '4':
            delete_transactions()#calling the delete function 
        elif choice == '5':
            display_summary()#calling the summary function
        elif choice == '6':
            filename = input("Enter the name of the file to read the bulk transactions : ")
            read_bulk_transactions_from_file(filename)

        elif choice == '7':
            #calling the class and the functions  in the imported py file
            root = tk.Tk()
            app = FinanceTrackerGUI(root)
            app.display_transactions()
            root.mainloop()
            
            
            
        elif choice == '8': 
            print("\nExiting program.")
            break #breaking the loop
        else:
            print("\nInvalid choice. Please try again.") #Error message

if __name__ == "__main__":
    main_menu()#calling the main function

