#!/usr/bin/python3

print("Enter a string and remove nth index")
x=input("enter  str:-")
y=input("enter index:-")
y=int(y)
z=len(x)
print(x[0:y:1] + x[y+1:z:1])

Output:-
Enter a string and remove nth index
enter  str:-hello team
enter index:-3
helo team