# employee payrroll program
employee_idinput = input("Enter employee ID: ")
employee_nameinput = input("Enter employee name: ")
basic_salaryinput = float(input("Enter base salary: "))
allowanceinput = float(input("Enter allowance: "))
deductioninput = float(input("Enter deduction: "))
# calculate gross salary, tax, and net salary
gross_salary = basic_salaryinput + allowanceinput
tax = gross_salary * 0.1  # Assuming a tax rate of 10%
net_salary = gross_salary - tax - deductioninput
print("Payslip")
print("Employee ID:", employee_idinput)
print("Employee Name:", employee_nameinput)
print("Base Salary:", basic_salaryinput)
print("Allowance:", allowanceinput)
print("Deduction:", deductioninput)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary) 