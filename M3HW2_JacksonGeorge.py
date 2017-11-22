#CTI 110
#M3HW2 - Software Sales
#George Jackson
#9/14/17

#A software company sells a package that retails for $99. They offer bulk discounts for volume purchases (for example, buying many copies to install in a college classroom). The discounts are as follows:
#Quantity 10-19: 	10% discount
#Quantity 20-49:	20% discount
#Quantity 50-99:	30% discount
#Quantity 100+:	        40% discount



userNumberOfPackages = int( input( "Please enter the number of pac" + \
                               "kages bought: " ) )
packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0
elif userNumberOfPackages < 20:
    discount = 0.10
elif userNumberOfPackages < 50:
    discount = 0.20
elif userNumberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = userNumberOfPackages * packagePrice 
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "Amount of discount: $" + format( discountAmount, ",.3f" ) + \
       "\nTotal amount: $" + format( total, ",.2f" ) ) 
