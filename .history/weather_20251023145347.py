import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Convert the ISO (year-month-day-hour-minutes-seconds-milliseconds) string into human format using the datetime module

    #Use datetime.fromisoformat() to convert the string to a datetime object, then use strftime() to format the date
    convert_date = datetime.fromisoformat(iso_string)
    # Format the date to the desired output
    date = convert_date.strftime("%A %d %B %Y")
    # Return the formatted date
    return date

# Example usage:
iso_string = ("2025-10-18T00:00:00.000")
new_date = convert_date(iso_string)
print(new_date)



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # Take the temperature in fahrenheit and convert it to a float if it is not already
    temp = float(temp_in_fahrenheit)
    # Convert it into Celcius using the formula (F-32)/1.8 
    celcius = (temp-32)/1.8
    # Round it to 1 decimal place
    rounded_celcius = round(celcius,1)
    # Return the rounded value
    return rounded_celcius

#Example usage 
temp_in_f = 61
celcius = convert_f_to_c(temp_in_f)
print (celcius)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # take the list i.e. the weather_data 
    numbers = [weather_data]
    print (numbers)

    # and calculate its mean
    # but since it is a list, you will have to loop through each number in the list 
    for num in numbers:
        # formula to calculate mean
        print(num)
        mean = sum(num)/len(num)
        return mean 

# Example usage: 
numbers = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
mean = calculate_mean(numbers)
print (mean)



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []

    # Open the csv file and read its contents
    with open(csv_file) as file:  
        # Use the csv module to read the file
        reader = csv.reader(file)
        next(reader)
        # Convert the reader object to a list
        for row in reader:
            # which means if there is content in the row i.e. if it is not empty, run the loop, otherwise ignore it - which ignores the empty lines 
            if row:
                current_date = row[0]
                current_min_temp = int(row[1])
                current_max_temp = int(row[2])
                data.append([current_date,current_min_temp,current_max_temp])

        return data

# Example usage:
data = load_data_from_csv("./tests/data/example_two.csv")
print (data)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    new_weather_data = [float(element) for element in weather_data]


    # Initialize min_value with first element of the list weather_data
    min_value = new_weather_data[0]
    min_index = 0

    # Iterate through the list to find the smallest element 

    for current_index, current_value in enumerate(new_weather_data):

        # If the current value is smaller than the current smallest value 

        if current_value <= min_value:
            min_value = current_value
            min_index = current_index
        
    return (min_value, min_index)


#  Example usage 
weather_data = [49, 57, 56, 55, 53]
result = find_min(weather_data)
print(result)


# Can do: 6
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    new_weather_data = [float(element) for element in weather_data]

    max_value = new_weather_data[0]
    max_index = 0

    for current_index, current_value in enumerate(new_weather_data):
        if current_value >= max_value:
            max_value = current_value
            max_index = current_index

    return(max_value, max_index)            

#  Example usage 
weather_data = [49, 57, 56, 55, 53]
result = find_max(weather_data)
print(result)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Handle an empty list
    if not weather_data:
        return "No forecast, take each day as it comes :p"
    
    # Find out the number of days
    num_of_days = len(weather_data)

    # Create empty lists for all the data we need to extract
    min_temp_c =[]
    max_temp_c = []
    iso_dates = []

    # Loop through the list of lists, set the indices for each data type
    # Then convert all the data in the extracted list to Celcius 
    # Now, append the values in the indices together, data with date, min temp with min temp etc 
    for day_temp in weather_data:
        iso = day_temp[0]
        min_f = day_temp[1]
        max_f = day_temp[2]
        min_c = convert_f_to_c(min_f)
        max_c = convert_f_to_c(max_f)
        date = iso
        min_temp_c.append(min_c)
        max_temp_c.append(max_c)
        iso_dates.append(date)

    # Now, I need to find the extremes + the day they occurred
    # Since find_min and find_max return a tuple of (value, index), I can unpack them into two variables each
    lowest_c, lowest_index = find_min(min_temp_c)
    highest_c, highest_index = find_max(max_temp_c)

    # Convert the index to the date using the iso_dates list
    lowest_date = convert_date(iso_dates[lowest_index])
    highest_date = convert_date(iso_dates[highest_index])


    # Now I need to get the averages of the min and max temp

    avg_low_c = calculate_mean(min_temp_c)
    avg_high_c = calculate_mean(max_temp_c)

    # Adding the degree symbol
    
    lowest_c_str = format_temperature(round(lowest_c,1))
    highest_c_str = format_temperature(round(highest_c,1))
    avg_low_str = format_temperature(round(avg_low_c,1))
    avg_high_str = format_temperature(round(avg_high_c,1))

    # write a summary

    summary = ""

    summary += f"{num_of_days} Day Overview\n"
    summary += f"  The lowest temperature will be {lowest_c_str}, and will occur on {lowest_date}.\n"
    summary += f"  The highest temperature will be {highest_c_str}, and will occur on {highest_date}.\n"
    summary += f"  The average low this week is {avg_low_str}.\n"
    summary += f"  The average high this week is {avg_high_str}.\n"
    return summary

    # First Attempt -incomplete
    # weather_data = []
    # lowest_temp_day = find_min(weather_data)
    # highest_temp_day = find_max(weather_data)
    # # Add a for loop here potentially 
    # list_lowest_temp = () 
    # list_highest_temp = ()
    # avg_low_combined = calculate_mean(list_lowest_temp)
    # avg_high_combined = calculate_mean (list_highest_temp)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "I'd rather you google it"
    
    summary_str = "" 

    for day_temp in weather_data:
        iso_date = day_temp[0]
        min_f = day_temp[1]
        max_f = day_temp[2]
        min_c = convert_f_to_c(min_f)
        max_c = convert_f_to_c(max_f)
        readable_date = convert_date(iso_date)

    
    
    