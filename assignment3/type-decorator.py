from functools import wraps

def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(int)
def add_int(a,b):
    return a + b

@type_converter(str)
def add_str(a,b):
    return a + b

# print(add_int(2,3))
# print(type(add_int(2,3)))
#print(add_str(2,3))
# print(type(add_str(3,3)))

@type_converter(str)
def return_int():
    return 5
result=return_int()
print(result)
print(type(result))

@type_converter(int)
def return_string():
    return "not a number"



if __name__ == "__main__":  
    y = return_int()
    print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen
   
