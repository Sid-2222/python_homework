# Task 1.2

import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
# To write a log record:

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        positional_parameters = list(args) if args else "none"
        keyword_parameters = kwargs if kwargs else "none"
        func_result = func(*args, **kwargs)
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {positional_parameters}\n"
            f"keyword parameters: {keyword_parameters}\n"
            f"return: {func_result}\n"         
            
        )
        
        logger.log(logging.INFO, log_message)
        return func_result
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

@logger_decorator
def greeting(name="World"):
    return f"Hello, {name}!"

#add(3,4)
#greeting("momo")
#greeting()

#Task 1.3

@logger_decorator
def hello():
    print("Hello World")

#hello()

# Task 1.4

@logger_decorator
def check_true(*args):
    return True

#Task 1.5

@logger_decorator    
def decorator(**kwargs):
    return logger_decorator

#Task 1.6

 if __name__ == "__main__":  
     check_true(1,2)
     decorator(a=1,b=2)
     hello()      

