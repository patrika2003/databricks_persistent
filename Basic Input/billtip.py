bill = float(input("Enter total bill: "))
tip_percent = float(input("Enter tip percentage: "))
tip = bill * tip_percent / 100
total = bill + tip

print("Tip:", tip)
print("Total Bill:", total)
