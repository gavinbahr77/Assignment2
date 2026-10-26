"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
AVERAGE_PACKERS_TICKET_PRICE = 180


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester = annual_cost / SEMESTERS_PER_YEAR
    return semester


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month = annual_cost / MONTHS_PER_YEAR
    return month


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return day


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit = annual_cost / (SEMESTERS_PER_YEAR * credits)
    return credit


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = annual_cost / (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER * credits / CS1430_CREDITS)
    return class_cost


def packers_tickets(annual_cost, ticket_price):
    """Give back how many Packers tickets you can buy with the annual cost."""
    tickets = annual_cost / AVERAGE_PACKERS_TICKET_PRICE
    return tickets


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits this semester: "))

    while True:
        # Show your menu here.
        print("Menu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Amount of packers tickets you can buy")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        # Add a branch for each menu option here.
        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            tickets = int(packers_tickets(annual_cost, AVERAGE_PACKERS_TICKET_PRICE))
            print(f"You can buy {tickets} Packers tickets.")
        else:
            print("Invalid choice. Please try again.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
