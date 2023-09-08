#calculate the year as leap year or not using if,elif,else
year = int(input("Enter Year:"))
if year % 4 == 0 and year % 100 != 0:
  print(year, "is a Leap Year")
elif year % 100 == 0:
  print(year, "is not a Leap Year")
elif year % 400 == 0:
  print(year, "is a Leap Year")
else:
  print(year, "is not a Leap Year")
