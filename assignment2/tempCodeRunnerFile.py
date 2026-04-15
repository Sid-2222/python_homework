import csv
import traceback

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
    return employees["fields"].index(column_name)

employee_id_column = column_index("first_name")
print(employee_id_column)

# Task 4

def first_name(row_number):
    index=column_index("first_name")
    return employees["rows"][row_number][index]

print(first_name(0))