import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2

def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            first = True
            for row in reader:
                if first:
                    data["fields"] = row
                    first = False
                else:
                    rows.append(row)

        data["rows"] = rows
        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
#print(employees)

#Task 3

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")
    

employee_id_column = column_index("employee_id")
#print(employee_id_column)

# Task 4

def first_name(row_number):
    try:
        index=column_index("first_name")
        return employees["rows"][row_number][index]
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")

#print(first_name(1))

# Task 5

def employee_find(employee_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id
            
        matches = list(filter(employee_match, employees["rows"]))
        return matches
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")
          
#print(employee_find(11))

# Task 6

def employee_find_2(employee_id):
    try:
         matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
         return matches
     
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")


#print(employee_find_2(2))

# Task 7

def sort_by_last_name():
    try:
        last_name_index = column_index("last_name")
        employees["rows"].sort(key=lambda row: row[last_name_index])
        return employees["rows"]
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")
               
#sort_by_last_name()
#print(employees)

# Task 8

def employee_dict(row):
  
        final_dict={}
        for key , value in zip(employees["fields"],row):
            if key != "employee_id":
                final_dict[key]=value
        return final_dict
      
    

#print(employee_dict(employees["rows"][1]))

# task 9

def all_employees_dict():
    final_dict_all={}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        final_dict_all[emp_id]=employee_dict(row)
    return final_dict_all


#print(all_employees_dict())

# Task 10

def get_this_value():
    return os.getenv("THISVALUE")
  

# Task 11

def set_that_secret(secret):
    custom_module.set_secret(secret)  
    
set_that_secret("Hsssss!!!! Its Top secret")
#print(custom_module.secret)

#Task 12

def read_csv_helper(csv_path):
    final_data={}
    rows=[]
    with open(csv_path,"r") as file:
        reader = csv.reader(file)
        first= True
        for row in reader:
            if first:
                final_data["fields"]= row
                first= False
            else:
                rows.append(tuple(row))
    final_data["rows"]=rows
    return final_data

def read_minutes():
    minutes1 = read_csv_helper("../csv/minutes1.csv")
    minutes2 = read_csv_helper("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

#print(minutes2)

# Task 13

def create_minutes_set():
    set1=set(minutes1["rows"])
    set2=set(minutes2["rows"])
    combain_set=set1.union(set2)
    return combain_set
minutes_set = create_minutes_set()
#print(minutes_set)

#Task 14

def create_minutes_list():
    min_list=list(minutes_set)
    return list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),min_list)
    )
minutes_list = create_minutes_list()
#print(minutes_list)

# Task 15

def write_sorted_list():
    sort_list = sorted(minutes_list, key=lambda x : x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),sort_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
final_minute = write_sorted_list()
#print(final_minute)