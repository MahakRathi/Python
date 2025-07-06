#Write a program that takes two numbers from the user and prints:
#their sum,
#difference,
#product, and
#division.

Number1=int(input("Enter 1st Number: "));
Number2=int(input("Enter 2nd Number: "));
Operator=input("Enter Operator Name: ");

if Operator=="+":
    print(Number1+Number2);
elif Operator=="-":
    print(Number1-Number2);
elif Operator=="*":
    print(Number1*Number2);
elif Operator=="/":
    print(Number1/Number2);
else:
    print("Invalid Input");