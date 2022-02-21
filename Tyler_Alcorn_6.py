# question 6

og_inches = float(input('Enter a number of inches ', ))

# getting miles total

miles = og_inches / (5280 * 12)

total_miles = int(miles)

leftover_miles =og_inches % (5280*12) #keeping unit as in

if total_miles >= 1:
    leftover_miles=og_inches-total_miles*5280*12
    print(total_miles, 'miles')


# getting total yards
yards = leftover_miles / (3 * 12)

total_yards = int(yards)

leftover_yards =  leftover_miles % (3 * 12)


if total_yards >= 1:
    leftover_yards=leftover_miles- total_yards*3*12
    print(total_yards, 'yards')


# getting total feet
feet = leftover_yards / 12

total_feet = int(feet)

leftover_feet =leftover_yards % (3 * 12)


if total_feet >= 1:
    leftover_feet=leftover_yards- total_feet*12
    print(total_feet, 'feet')

# getting total inches
if leftover_feet >= 1:
    print(leftover_feet, 'inches')
