#CTI-110
#M2HW2 - Tip Tax Total
#George Jackson
#9/7/17


foodCharge = float( input("Please enter the charge of the food: ")) 

tipAmount = 0.18 * foodCharge 

salesTax = 0.07 * foodCharge


totalCost = foodCharge + tipAmount + salesTax

print( "Food Charge: $" + format( foodCharge, ",.2f"), "Tip Amount: $" + \
       format( tipAmount, ",.2f"), "Sales Tax: $" + format( salesTax, ",.2f"),  \
       "Total Cost: $" + format( totalCost, ",.2f"), )




