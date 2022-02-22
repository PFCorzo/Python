## Financial Summary

### Convert the csv into a dictionary to manipulate key value pairs
budget_data_dict = dict() 
budget_data_csv = open("./Resources/budget_data.csv") # Use python open function to make csv file python readable 
for line in budget_data_csv: 
    line = line.strip('\n')
    (key, val) = line.split(",")   
    budget_data_dict[key] = val
print(budget_data_dict) 
