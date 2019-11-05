
#ryan yu
"""This program allows multiple employees to enter their respective hours worked and hourly rate to return their pay,
and will sum up total pay of all the employees and the average pay between the employees"""


def main() -> None:
    """This function prompts the user to input the number of emplyees, then puts together all the calculations to print the total pay within all employees and the average pay"""  
    i = 1
    num_of_employees = int(input("How many emloyees do you want to enter? "))
    total_pay = 0
    
    while (i <= num_of_employees):
        name, hours, hourate = get_input()
        pay = calc_pay(hours, hourate)
        print_pay(name, pay) 
        total_pay += pay
        i += 1
    print()
    print("The total amount to be paid is ${:,.2f}". format(total_pay))
    print("The average employee is paid ${:,.2f}". format(total_pay / num_of_employees))

def get_input() -> tuple:
    """This function prompts the employees to input their hours, rate, and name"""
    print()
    name = input("Enter a name: ")
    hrs = float(input("Enter hours worked: "))
    hrt = float(input("Enter hourly rate: "))
    return (name, hrs, hrt)

def calc_pay(hours: float, rate: float) -> float:
    """this function uses the hours and rate of each employee to calcute their individual pay."""
    if (hours > 40):
        return ((40 * rate) + ((hours - 40) * (1.5 * rate)))
    else:
        return (hours * rate)
    

def print_pay(name: str, pay: float) -> None:
    """this function prints the name and pay of that respective employee"""
    print(str(name), "should be paid ${:,.2f}". format(pay))

if __name__ == "__main__":
    
    print (__doc__)
    print()
    main()
    print()
    input("press enter to continue...")
    functions=[main, get_input, calc_pay, print_pay]
    for x in functions:
        print()
        print (x.__name__)
        print (x.__doc__)
        print (x.__annotations__)
        
        



