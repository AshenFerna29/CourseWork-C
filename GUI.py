#importing tikinter 
import tkinter as tk
from tkinter import ttk
#importing tikinter message box
from tkinter import messagebox
#importing json 
import json

#creating a main class for all the functions
class FinanceTrackerGUI:
    #defining a function for the GUI main window
    def __init__(self, root):
        self.root = root
        
        
        width,height = 650,650 #creating the size

        #instructions to open the window in the middle of the screen 
        display_width = self.root.winfo_screenwidth()
        display_height = self.root.winfo_screenheight()
        left  = int(display_width/2 - width/2)
        top = int(display_height/2 - height/2)
        self.root.geometry(f'{width}x{height}+{left}+{top}')

        #creating a window title
        self.root.title("Personal Finance Tracker")
        #disabling the resizability
        self.root.resizable(False,False)
        
        self.transactions = {}
        
        #calling the function
        self.create_widgets()

        #calling the json file
        self.load_transactions("coursework2.json")



    #creating all the widgets for the window 

    def create_widgets(self):
        
        # Frame for table and scrollbar
        self.tree_frame = tk.Frame(self.root,background='#D06AFC')
        self.tree_frame.pack(fill = "x",pady=10)

        label = tk.Label(self.tree_frame,text= "Personal Finance Tracker",font=("Harlow Solid Italic",20),background='#D06AFC')
        label.pack(ipady=5)

        self.tree_frame1 = tk.Frame(self.root)
        self.tree_frame1.pack(fill="x",pady=10)

        label1 = tk.Label(self.tree_frame1,text="Transaction Which you have made so far",font=("Times New Roman",15))
        label1.pack(padx=10)


        # Treeview for displaying transactions
        self.table =ttk.Treeview(self.root, columns=('amount','date','category'),show = 'headings',) 
        #creating the  columns 
        self.table.heading('amount', text="Amount",command=lambda:self.sort_by_column("amount"))
        self.table.heading('date',text="Date",command=lambda:self.sort_by_column("date"))
        self.table.heading('category',text="Category",command=lambda:self.sort_by_column("category"))
        self.table.column('amount',width=100)
        self.table.column('date',width=100)
        self.table.column('category',width=100)
        
        
        

        

        self.table.pack(fill="x",pady=50)#packing the table for the window
        


        # Scrollbar for the Treeview
        scroll_bar = ttk.Scrollbar(self.table,orient='vertical',command=self.table.yview)
        scroll_bar.pack(side='right',ipady=50)
        self.table.configure(yscrollcommand=scroll_bar.set)

        # Search bar and button
        self.search_entry = tk.StringVar()
        search_entry = ttk.Entry(self.root,textvariable=self.search_entry)
        search_entry.pack()
        search_button = ttk.Button(self.root, text="Search",command=self.search_transactions)
        search_button.pack()

        self.frame  =tk.Frame(self.root)
        self.frame.pack(fill="x")

        label2 = tk.Label(self.frame, text="Press The Headings of the table to sort !",font=("Times New Roman",15),background="#9AF85D",padx=650)
        label2.pack(pady=20)
        #creating a reset button and packing it to the window 
        reset_button = tk.Button(self.root,text="Reset",command=self.reset_transactions,background="#5DD5F8")
        reset_button.pack()

        pass
        
    #crearting a function to load the json file 
    def load_transactions(self, filename):
        try:
            with open(filename, "r") as f:
                self.transactions = json.load(f)  # Load transactions from the file
        # If the file doesn't exist, initialize an empty dictionary
        except FileNotFoundError:
            self.transactions={}
        
            
            
    
    #ccreating a function to display the transactions in the window
    def display_transactions(self):
         # Remove existing entries
        for item in self.table.get_children():#creating a loop
            self.table.delete(item)
   
    # Add transactions to the treeview
        for category, transactions in self.transactions.items():#creating a loop
            for transaction in transactions:#creating a loop
                self.table.insert('', "end", values=(transaction['amount'], transaction['date'],category))#inserting the values to the table 



    def search_transactions(self):
        # Placeholder for search functionality
        search_transaction = self.search_entry.get().capitalize()#capitalizing the user inputs 

        for data in self.table.get_children():#creating a loop
            self.table.delete(data)

        reuslt_found = False #checking the input 

        for category, values in self.transactions.items():#creating a loop
            for transaction in values:#creating a loop
                if ( search_transaction in str(transaction["amount"]) or search_transaction in str(transaction["date"])or search_transaction in str(category)):
                    self.table.insert('', "end", values=(transaction['amount'], transaction['date'], category))
                    reuslt_found = True

        if not reuslt_found:#creating a error message box
            messagebox.showinfo(title="Invalid Input",message="Search Not Found!")#adding the string to the meesage box


        


        

        pass
 
    #creating a function to sort the transactions in ascending order
    def sort_by_column(self,column):
        
    
        # Prompt user for sorting order
        sort_order = messagebox.askquestion("Sort Order", f"Do you want to sort '{column}' column in ascending order?")
        
        # Determine the sorting order based on user input
        reverse = False if sort_order == "yes" else True

        # Get data from the table
        data = [(self.table.set(child, column), child) for child in self.table.get_children("")]
        
        # Sort the data
        data.sort(reverse=reverse)
        
        

        # Rearrange the rows in the table
        for i, (val, child) in enumerate(data):#creating a loop
            self.table.move(child, "", i)
        
        # Update the heading command to toggle the sorting order
        self.table.heading(column, command=lambda: self.sort_by_column(column))



    #creating a function to reset the trasnavtions 
    def reset_transactions(self):

        self.search_entry.set("")
        self.display_transactions()
        
        
        
           
            
#creating a main function to run the code
def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions()
    root.mainloop()

if __name__ == "__main__":
    main()