"""
Qn.
Write a program to capture the expenditure(How much money spent) of each individual at home on the following expenses: food, transport, airtime and mobile data. The program should compute the total and average expenditure of all expenses
"""

FOOD = "food"
TRANSPORT = "transport"
AIRTIME = "airtime"
DATA = "data"

expenses = [FOOD, TRANSPORT, AIRTIME, DATA]

food_expenditure = 0
transport_expenditure = 0
airtime_expenditure = 0
data_expenditure = 0

family_member_count = 0

while True:
    family_member_name = input("\nEnter name of family member: ")
    for expense in expenses:
        expenditure = int(input(f"\tEnter your {expense} expenditure: "))
        if expense == FOOD:
            food_expenditure += expenditure
        elif expense == TRANSPORT:
            transport_expenditure += expenditure
        elif expense == AIRTIME:
            airtime_expenditure += expenditure
        elif expense == DATA:
            data_expenditure += expenditure
    family_member_count += 1

    more_family_memebers = input("\nDo you have any other family member? (y/n) ")
    if more_family_memebers == 'n':
        break

average_food_expenditure = food_expenditure/family_member_count
average_transport_expenditure = transport_expenditure/family_member_count
average_airtime_expenditure = airtime_expenditure/family_member_count
average_data_expenditure = data_expenditure/family_member_count

print(f"\nFood Expenditure: {food_expenditure}\t\tAverage Food Expenditure: {average_food_expenditure}")
print(f"Transport Expenditure: {transport_expenditure}\tAverage Transport Expenditure: {average_transport_expenditure}")
print(f"Airtime Expenditure: {airtime_expenditure}\tAverage Airtime Expenditure: {average_airtime_expenditure}")
print(f"Data Expenditure: {data_expenditure}\t\tAverage Data Expenditure: {average_data_expenditure}")

