salesperson_name = input("Salesperson's name: ")
salesperson_num = input("Salesperson's number: ")
salesperson_sales = int(input("Salesperson's weekly total sales: "))

FIVE_MILLION_LIMIT = 5000000 # 5 million
BASE_PAY = 1000000 # 1 million

salesperson_pay = BASE_PAY
if salesperson_sales <= FIVE_MILLION_LIMIT:
    salesperson_pay += (0.1 * salesperson_sales)
else:
     extra_sales = salesperson_sales - FIVE_MILLION_LIMIT
     salesperson_pay += (0.1 * FIVE_MILLION_LIMIT) + (0.15 * extra_sales)

print(f"\nSalesperson Name: {salesperson_name}\nSalesperson Number: {salesperson_num}\nSalesperson Pay: {salesperson_pay}")