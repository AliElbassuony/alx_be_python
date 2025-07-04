from datetime import datetime
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def display_current_datetime():
    
    print(f"Current date and time: {current_date}")
    

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.timedelta(days=number_of_days) + datetime.date.today()
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

display_current_datetime()

calculate_future_date()