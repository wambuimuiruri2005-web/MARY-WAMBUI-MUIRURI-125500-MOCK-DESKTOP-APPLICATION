cows=int(input("Enter the number of cows: "))
milk_per_cow=float(input("Enter the amount of milk produced per cow per day (in liters): "))
cost_perliter=float(input("Enter the cost per liter of milk: "))
total_milk = cows * milk_per_cow
total_cost = total_milk * cost_perliter
print("Milk Production Report")
print("total milk produced per day:", total_milk, "liters")
print("total cost of milk production per day:", total_cost, "currency units")