#Task 1
name="Watzit Tooya";
age=42;
height=6.9;

print("Hello.  My name is " + name + ", I'm " + str(age) + " years old, and I am " + str(height) + " feet tall.\n")

#Task 2
numA=42;
numB=69;

print("The sum of " + str(numA) + " and " + str(numB) + " is " + str(numA + numB));
print("The difference between " + str(numB) + " and " + str(numA) + " is " + str(numB - numA));
print(str(numA) + " multiplied by " + str(numB) + " is " + str(numB * numA));
print(str(numB) + " divided by " + str(numA) + " is " + str(numB / numA));
print("\n");

#Task 3
num=float(input("Please input a number.\n"));

if num>0:
    print("This number is positive.  Awesome!");
elif num<0:
    print("This number is negative.  Better luck next time!")
else:
    print("Zero it is.  A perfect balance!");