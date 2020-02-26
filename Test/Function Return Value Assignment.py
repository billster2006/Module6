def hourly_employee_input():  # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name: ")  # user input string
    hours_worked = int(input("Please enter your hours worked: "))  # user input int, possible ValueError
    hourly_rate_pay = float(input("Please enter your rate of pay: "))  # user input float, possible ValueError
    func_return = weekly_pay()
    print(name, func_return)


def weekly_pay(hours, pay):
    hours, pay = hourly_employee_input()
    weekly_pay_amount = hours * pay
    return weekly_pay_amount



if __name__ == '__main__':
    hourly_employee_input()
    weekly_pay()
