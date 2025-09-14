prompt_monthly_income = input("Enter your monthly income:")
monthly_income = int(prompt_monthly_income)
prompt_monthly_expenses = input("Enter your total monthly expenses:")
monthly_expenses = int(prompt_monthly_expenses)
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print("Your monthly savings are", monthly_savings,)
print("Projected savings after one year, with interest, is:", projected_annual_savings)