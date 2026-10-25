print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip_percentage = int(input("what percentage tip?"))
people = int(input("How many people are splitting?"))
tip_amount = bill * tip_percentage / 100
total_bill = bill + tip_amount
amount_per_person = total_bill / people
print(f"Total bill including tip: ${total_bill:.2f}")
print(f"Each person pays ${amount_per_person:.2f}")

