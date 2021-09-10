#!/usr/bin/python3

print("Check Electricity Bill Amount")
x=int(input("enter Customer Id:-"))
y=input("enter Name:-")
c=int(input("Unit:-"))
Amount=0
if c<=199:
 Amount= c*1.20
elif c>=200:
 if c<400:
  Amount = c*1.50
 elif c>=400:
  if c<600:
   Amount=c*1.80
  elif c>=600:
   Amount = c*2.00
if Amount>400:
  z = (Amount*15)/100
  Amount =z + Amount
  print("Amount =",Amount)
else:
 print("Amount:",Amount + 100)

Output:-
Check Electricity Bill Amount
enter Customer Id:-45
enter Name:-k
Unit:-400
Amount = 828.0

Check Electricity Bill Amount
enter Customer Id:-45
enter Name:-k
Unit:-200
Amount: 400.0
