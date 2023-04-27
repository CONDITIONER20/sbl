import employee
basic_salary = 50000
da = 0.1 * basic_salary
hra = 0.05 * basic_salary
tax = 0.02 * basic_salary
gross_salary = employee.calculate_gross_salary(basic_salary, da, hra)
net_salary = employee.calculate_net_salary(gross_salary, tax)
print("Basic salary:", basic_salary)
print("Gross salary:", gross_salary)
print("Net salary:", net_salary)
