# The year can be evenly divided by 4, is a leap year,
# The year can be evenly divided by 100, it is NOT a leap year, 
# The year is also evenly divisible by 400. Then it is a leap year
# the years 2000 and 2400 are leap years
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

year = int(input("Please enter Year: "))
flag = False

if year%400 == 0 and year%100 == 0:
    flag = True
elif year%4 == 0 and year%100 != 0:
    flag = True

print(flag)


