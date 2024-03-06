#calculate budget based on paycheck

def main():
	#gather information 
	total_pay = float(input("Enter pay for this pay period: "))
	credit_balance = float(input("Enter your credit line balance: "))

	#calculate percentage of how much goes to credit card
	credPayment = (credit_balance * 0.2)

	#calculate percentage of minimum saving for the check
	biweeklySavingMin = total_pay * 0.1
	print(f"Save at least {biweeklySavingMin} this month")
	
	#calculate how much is left over
	total_pay = total_pay - credPayment - biweeklySavingMin - 30 - 30
	print(f"Leftover before setting aside for rent: {total_pay}")

	if total_pay >= 350 : 
		total_pay -= 350

	else:
		total_pay -= 250
	print(f"After setting aside money for rent: {total_pay}")

if __name__ == '__main__':
	main()