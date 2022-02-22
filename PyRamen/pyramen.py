# Import Dependencies
import csv 
from os import read 
from pathlib import Path

# Set path for data provided 
menu_path = Path('./Resources/menu_data.csv') 
sales_path = Path('./Resources/sales_data.csv') 

# Create a function that will read the data, and return into a list 

def data(): 
    menu_column = [] #Declare variable as list
    sales_column = [] # Decclare variable as list

    with open(menu_path, 'r') as menu: 
        readable_menu = csv.reader(menu) 
        next(readable_menu) 
        for row in readable_menu:
            menu_column.append(row)

    with open(sales_path, 'r') as sales:
        readable_sales = csv.reader(sales)
        next(readable_sales) 
        for row in readable_sales: 
            sales_column.append(row) 
    return menu_column,sales_column 

#Create a function that 

def main(menu_column, sales_column):
    report = {}
    items = [] 
    for row in sales_column: # Initialize for loop
        Quantity = int(row[3]) 
        Menu_items = row[4]
        if Menu_items not in report: #Conditional for Sales column
            report[Menu_items] = { "01-count":0,"02-revenue":0,"03-cogs":0, "04-profit:0":0,} 

    for row in menu_column: # Initialiaze second loop  
        Item = row[0]
        Price = float(row[3]) 
        Cost = int(row[4])
        if Menu_items == items: #Conditional for Menu column  
            Price = Profit - Cost
            report[Menu_items]["01-count"] += Quantity
            report[Menu_items]["02-revenue"] += Price*Quantity
            report[Menu_items]["03-cogs"] += Cost*Quantity 
            report[Menu_items]["04-profit"] += Profit*Quantity
        else: 
            print(f"The items {Menu_items} and {Item} are not same. Appending 0 as Value")  
   
    Save_in_Directory = open("./Financial_Report.txt", "w", newline='')  
    for Menu_items in sales_column: 
        items.append(Menu_items[4]) 
    Clean_Duplicate = list(dict.fromkeys(items))

    for extra in range(len(Clean_Duplicate)):
        Save_in_Directory.write(Clean_Duplicate[extra]+""+str(report[Clean_Duplicate[extra]])+'\n') 

if __name__ == '__main__': 
    menu_column,sales_column = data()
    main(menu_column,sales_column) 
