#!/usr/bin/python3

print("Enter a string if having Not and poor than replace whole with good")
x=input("enter  str:-")
s= "Good"
s1="not"
s2="poor"
y=x.find(s1)
if y>0:
  p=x.rfind(s2)
  if p>0:
     print(x[:y]+s)
else:
  print(x)

Output:-
Enter a string if having Not and poor than replace whole with good
enter  str:-the lyrics is not that poor!
the lyrics is Good

Enter a string if having Not and poor than replace whole with good
enter  str:-the lyrics is poor
the lyrics is poor
