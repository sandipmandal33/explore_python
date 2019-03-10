my_var=33
print(my_var)

my_var="Sandip's var"
print(my_var)

def my_func():
    global my_var
    print(my_var)
    my_var="Sandip's func_var"
    print(my_var)

my_func()
print(my_var)

del my_var
#print(my_var)