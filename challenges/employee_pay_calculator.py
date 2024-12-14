MANAGER_PAY_CODE = "1"
HOURLY_WORKER_PAY_CODE = "2"
COMMISSION_WORKER_PAY_CODE = "3"
PEICE_WORKER_PAY_CODE = "4"

MANAGER_WEEKLY_PAY = 1500 # $1500 Per Week
HOURLY_PAY = 300 # $300 Per Hour
PIECE_WORKER_PAY_RATE = 200 # $200 Per Item
NORMAL_WORKING_HOURS_LIMIT = 40
COMMISSION_WORKER_BASE_PAY = 250 # $250

employee_pay = 0

employee_pay_code = input("Enter employee pay code: ")
if employee_pay_code == MANAGER_PAY_CODE:
    # Paying a manager
    employee_pay = MANAGER_WEEKLY_PAY
elif employee_pay_code == HOURLY_WORKER_PAY_CODE:
    # Paying an hourly worker
    num_hours_worked = int(input("How many hours worked? "))
    if num_hours_worked <= NORMAL_WORKING_HOURS_LIMIT:
        employee_pay = num_hours_worked * HOURLY_PAY
    else:
        employee_pay = (NORMAL_WORKING_HOURS_LIMIT * HOURLY_PAY)
        overtime_hours = num_hours_worked - NORMAL_WORKING_HOURS_LIMIT
        employee_pay += 1.5 * (HOURLY_PAY * overtime_hours)
elif employee_pay_code == COMMISSION_WORKER_PAY_CODE:
    # Paying a commission worker; Every commission workers is entitled to a base pay and a 5.7% of their gross weekly sales
    gross_weekly_sales = int(input("What are the employee's weekly sales?: "))
    employee_pay = COMMISSION_WORKER_BASE_PAY + (0.057 * gross_weekly_sales)
elif employee_pay_code == PEICE_WORKER_PAY_CODE:
    # Paying a pieceworker; pieceworkers are paid based on the number of items they sold
    num_items = int(input("How many items worked on?: "))
    employee_pay = PIECE_WORKER_PAY_RATE * num_items
else:
    print("Invalid employee pay code")

print(f"The pay is: {employee_pay}")
