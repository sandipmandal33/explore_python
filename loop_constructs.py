def my_range_func():
    for i, val in enumerate(range(1, 10)):
        print("Pos: ", i, " Value: ", val)

def my_collection_func(days):
    for curr_day in days:
        print("Current day: ", curr_day)

def my_variable_args_func(*args):
    for curr_arg in args:
        print("Current arg: ", curr_arg)

my_range_func()
print()

days=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
my_collection_func(days)
print()

my_variable_args_func(33, 66)
my_variable_args_func(33)
my_variable_args_func(33, 66, 99)
print()
