def hourly_employee_input():  # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name: ")  # user input string
    hours_worked = int(input("Please enter your hours worked: "))  # user input int, possible ValueError
    hourly_rate_pay = float(input("Please enter your rate of pay: "))  # user input float, possible ValueError
    print(name, hours_worked, hourly_rate_pay, ".")  # print statement, minial formatting


if __name__ == '__main__':
    try:  # check for ValueError
        hourly_employee_input()  # function call
    except ValueError as err:
        print("ValueError encountered! ")
