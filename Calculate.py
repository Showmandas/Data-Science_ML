#Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
opt=input("Enter an operator(+,-,*,/) which you want for calculation : ")

if opt=="+":
    print("The addition is : ",n1+n2)
elif opt == "-":
    print("The subtraction is : ",n1-n2)
elif opt == "*":
    print("The multiplication is : ",n1*n2)
else:
    print("The division is : ",n1/n2)
