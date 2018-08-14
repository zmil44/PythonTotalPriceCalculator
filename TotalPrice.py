'''
Zach Miller
9/3/13
CIS-127
'''
item1=float(input("Enter the price for Item 1:"))
item2=float(input("Enter the price for Item 2:"))
item3=float(input("Enter the price for Item 3:"))
item4=float(input("Enter the price for Item 4:"))
item5=float(input("Enter the price for Item 5:"))
subtotal=(item1+item2+item3+item4+item5)
tax=(subtotal*.06)
total=(subtotal+tax)
print('Subtotal:',format(subtotal,'.2f'))
print('Sales Tax:',format(tax,'.2f'))
print('Total:',format(total,'.2f'))
