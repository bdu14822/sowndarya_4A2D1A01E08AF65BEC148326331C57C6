#python program to check leap year
year=int(input("enter year to be checked:"))
if(year%400==0 and year%200==0):
  print("it is a century year and also a leap year")
elif(year%4==0 and year%100!=0):
  print("it is not a century year but it is leap year")
else:
  print("the year isn't a leap year!")