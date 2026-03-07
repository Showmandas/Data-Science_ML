#Write a program using a for loop that calculates the sum of even numbers between 1 and 100.

s=0
for i in range(1,101):
    if i%2==0:
        s+=i
print("The sum of even numbers : ",s)