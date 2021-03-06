# START LAB EXERCISE 03
print('Lab Exercise 03 \n')

# This week is the begining of the Chinese New Year and
# the Spring Festival. Let's learn more!
# We are writing a function with two positional arguments here.
# (Learn about python functions: https://www.w3schools.com/python/python_functions.asp)

# SETUP (DO NOT CHANGE)
# This is your global variable that can be reached from anywhere in the program.
# In this class we will be using all capital letters for global variables.
LUNAR_YEAR = "2020"

# END SETUP

# Refer to Lab Exercise 03 README.md for instructions and tips.

# PROBLEM 1.0 (5 points)

# BEGIN PROBLEM 1.0 SOLUTION
# 1.2.1 Write the header for the < lunar_new_year() > function

def lunar_new_year(year, year_animal):

    # Indent within the function!

    # 1.2.2 Implement < lunar_new_year() >
    # Use the < global > keyword if you want to modify a global variable inside a function.

    global LUNAR_YEAR
    LUNAR_YEAR = "{} is the year of {}.\n".format(year,year_animal)

    # 1.2.3 Return < LUNAR_YEAR >
    return LUNAR_YEAR


# END PROBLEM 1.0 SOLUTION

# You have created your first python function! Let's go further

# PROBLEM 2.0 (10 points)

# BEGIN PROBLEM 2.0 SOLUTION

# 2.2.1 & 2.2.2 Write the header for the < festivities_info() > function with default arguments
def festivities_info(date_start = "8-Feb", message = "Lantern Festival"):

    # Make sure you indent first!
    # 2.2.3 Assign default agruments using f-string
    new_message = (f"{date_start} is the day of {message}.\n")

    # 2.2.4 Return < new_message >
    return new_message


# END PROBLEM 2.0 SOLUTION

# Great! We have two function, now let's call them.

# SETUP (DO NOT CHANGE)
# This is the main function that will be called when the program runs.
def main():

# END SETUP

# PROBLEM 3.0 (5 points)

# We will be calling < lunar_new_year() > and < festivities_info() > functions

# BEGIN PROBLEM 3.0 SOLUTION

    # 3.2.1 Print global variable < LUNAR_YEAR >
    print(LUNAR_YEAR)

    # 3.2.2 Call < lunar_new_year() > function
    print(lunar_new_year(2020,"rat"))

    # 3.2.3 Call < festivities_info() > function
    print(festivities_info(date_start="February 8"))

    # 3.2.4 Print global variable < LUNAR_YEAR >
    # Observe changes of the global variable.
    print(LUNAR_YEAR)


# LAB 3.0 SETUP (DO NOT CHANGE)

if __name__== "__main__":
    main()

# END LAB EXERCISE
