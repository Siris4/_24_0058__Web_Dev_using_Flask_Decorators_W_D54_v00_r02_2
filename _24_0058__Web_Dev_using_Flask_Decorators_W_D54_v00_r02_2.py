import time

i = ""

current_time = time.time()
print(current_time)  # seconds since 12:00am on Jan 1st, 1970


# Write your code below 👇
def outter_function(main_function):
    def speed_calc_decorator():

        print(f"Starting time for {main_function.__name__} is: {time.time()}")
        before_processing = main_function()

        # return main_function()
        print(f"Ending time for {main_function.__name__} is: {time.time()}")
        # after_processing = main_function
        return before_processing

        #
        # time_difference = current_time - __name__[0]
        #
        # print(f"__name__ = {__name__}")


        # return time_difference()
    return speed_calc_decorator

@outter_function
def fast_function():
    for i in range(1000000):
        i * i

@outter_function
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
