def my_func_simple(arg):
    if(arg < 0):
        msg = "I am in simple function"
    else:
        msg = "I am in complex function"

    return msg

def my_func_defult_args(arg1, arg2=100):
    if(arg2 == 100):
        msg = "Default argument applied"
    elif(arg1 > arg2):
        msg = "First argument is greater"
    else:
        msg = "Second argument is greater"

    return msg       

print(my_func_simple(10))
print(my_func_defult_args(50))
print(my_func_defult_args(50, 500))