# Write your code here.
# Task 1
def hello():
    return "Hello!"
print(hello())


# Task 2
def greet(input):
    return "Hello, " + input + "!"
print(greet("momo"))


# Task 3
def calc(input1, input2, operation="multiply"):
    try:
        if operation == "add":
            return input1 + input2
        elif operation == "subtract":
            return input1 - input2
        elif operation == "multiply":
            return input1 * input2
        elif operation == "divide":
            return input1 / input2
        elif operation == "modulo":
            return input1 % input2
        elif operation == "int_divide":
            return input1 // input2
        elif operation == "power":
            return input1 ** input2
        else:
            return "invalid operation"
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
       return("You can't multiply those values!")


print(calc(10, 4, "divide"))

# Task 4

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return  int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return (f"Invalid Data type {data_type}")
    except(TypeError,ValueError):
        return (f"You can't convert {value} into a {data_type}.")

print(data_type_conversion("77","float"))

# Task 5

def grade(*args):
      try:
        result = sum(args) / len(args)
        if result >= 90:
            return "A"
        elif result >=80:
            return "B"
        elif result >=70:
            return "C"
        elif result >=60:
            return "D"
        else:
            return "F"
      except TypeError:
          return ("Invalid data was provided.")

print(grade(59))

# Task 6

def repeat( string , count):
    if count == 0:
        return ("Count can't be Zero ! Pleasw give a proper input !")

    try:
        new_string=""
        for i in range(count):
            new_string = new_string+string
        return new_string
    except (TypeError):
        return ("Invalid Input !! Plase check the input values !")

print(repeat("hello ",3))

# Task 7

def student_scores(position , **kwargs):
    if position == "best":
        best_student = ""
        best_score=0
        for student , score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = student
        return best_student

    elif position == "mean":
        total_score = 0
        student_count = 0
        for student, score in kwargs.items():
            total_score += score
            student_count += 1
        return total_score / student_count
    else:
        return("Invalid Position")  

print(student_scores("mean", Ali=93, Bob=85, jam=99, sam=100))

# Task 8

def titleize(input):
    new_split=input.split()
    exception_word =  ["a", "on", "an", "the", "of", "and", "is", "in"]    
    for i, word in enumerate(new_split):
        if word in exception_word:
            new_split[i] = new_split[i].lower()
        else:           
            new_split[i] = new_split[i].capitalize()
                        
    new_split[-1] = new_split[-1].capitalize()
    new_split[0] = new_split[0].capitalize()        
    return " ".join(new_split)

print(titleize("in curious incident of the dog in the night"))
print(titleize("the hollow chocolate bunnies of the apocalypse"))

# Task 9

def hangman(secret , guess):
    result_string = ""
    for i in secret:
       if i in guess:
           result_string = result_string+i
       else:
           result_string = result_string+ "_"
    return result_string

print(hangman("Califonia" , "lio"))

#task 10

def pig_latin(input):
    vowels = "aeiou"
    final_result = []
    words = input.split()
    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else:
            count = 0
            while count < len(word):
                if word[count: count + 2] == "qu":
                    count = count + 2
                elif word[count] not in vowels:
                    count = count +1
                else:
                    break
            new_word= word[count:] + word[:count] + "ay"
        final_result.append(new_word)
    final_output = " ".join(final_result)
    return final_output

print(pig_latin("hello momo queen ttal"))               
    