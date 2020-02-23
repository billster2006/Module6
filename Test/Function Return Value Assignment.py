def hourly_employee_input():  # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name: ")  # user input string
    hours_worked = int(input("Please enter your hours worked: "))  # user input int, possible ValueError
    hourly_rate_pay = float(input("Please enter your rate of pay: "))  # user input float, possible ValueError
    return hours_worked, hourly_rate_pay


def weekly_pay():
    hours, pay = hourly_employee_input()
    weekly_pay_amount = hours * pay
    print(weekly_pay_amount)


if __name__ == '__main__':
    try:  # check for ValueError
        display_string = hourly_employee_input()  # function call, store in a variable
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)  # print the result of the function
