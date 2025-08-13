# Generator: (expression for item in iterable if condition)
# like a stream they are

daily_sales = [5,10,12,23,4,2,31,21,32,112,3,22]
# total_cups = [sale for sale in daily_sales if sale > 5]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)