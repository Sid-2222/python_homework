import csv
employee_data_list=[]
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        employee_data_list.append(row)
        
                
#print(employee_data_list)

full_employee_names = [row[1] + " " + row[2] for row in employee_data_list[1:]]

print(full_employee_names)

name_has_e = [row for row in full_employee_names if "e" in row]

print(name_has_e)