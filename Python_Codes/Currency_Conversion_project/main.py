
print(
    """Here is a list of global currencies : \n 
1.USD: US Dollar ($)
2.EUR: Euro (€)
3.GBP: British Pound Sterling (£)
4.JPY: Japanese Yen (¥)
5.AUD: Australian Dollar ($)
6.CAD: Canadian Dollar ($)
7.CHF: Swiss Franc (Fr)
8.CNY: Chinese Yuan (¥)
9.INR: Indian Rupee (₹)
10.RUB: Russian Ruble (₽)"""
)

n=int(input("Choose currency for converting to Taka(৳) from the list by entering 1/2/3... : " ))

if n==1:
    print("1 Taka = 0.0082 ($)")
    user_choice=input("you want to convert Taka to USD? Type yes/no")
    if user_choice=="yes":
       user_input=float(input("Enter your amount in taka : "))
       usd=float(user_input * 0.0082)
       print(f"{usd} $")
    else:
        user_input=float(input("Enter your amount in USD : "))
        print(f"{user_input/0.0082} ৳")
