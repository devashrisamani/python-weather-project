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

    # and calculate its mean
    mean = sum(numbers)/len(numbers)
    return mean 

# Example usage: 
numbers = [1,2,3,4,5,6]
mean = calculate_mean(numbers)
print (mean)




# Can do, do it another file to check the output: 4
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

# Can do: 5
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


# Can do: 6
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass

# Can do: 7 - Google how to handle multi-line f strings and making paragraphs - you can check the output files and test examples to see what this file expects 
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


# Can do: 8 
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
