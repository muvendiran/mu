bala1 = float(input("Enter first number: "))
bala2= float(input("Enter second number: "))
bala3 = float(input("Enter third number: "))
 
if (bala1 > bala2) and (bala2 > bala3):
   largest = bala1
elif (bala2 > bala1) and (bala2 > bala3):
   largest = bala2
else:
   largest = bala3
 
print("The largest number is",largest)
