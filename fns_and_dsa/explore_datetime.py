# Import datetime module
import datetime

# PART ONE (1)
def display_current_datetime():

# save the current date inside a current_date variable
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}") # Print in a specific format
    return current_date

# PART TWO (2)
def calculate_future_date():

    current_date = display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


# call the function
calculate_future_date() 
