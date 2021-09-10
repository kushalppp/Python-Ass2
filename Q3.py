#!/usr/bin/python3

print("Enter a string if is 3 letter add ing and if already ing add ly")
x=input("enter  str:-")
s= "ing"
z= "ly"
y = len(x)
if y>2:
  p=x.rfind(s)
  if p == -1:
     print(x + s)
  else:
     print(x + z)
else:
  print("string length less than 3")

Output:-
Enter a string if is 3 letter add ing and if already ing add ly
enter  str:-str
string
Enter a string if is 3 letter add ing and if already ing add ly
enter  str:-string
stringly
Enter a string if is 3 letter add ing and if already ing add ly
enter  str:-st
string length less than 3