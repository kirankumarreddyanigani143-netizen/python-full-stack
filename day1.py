m1=int (input("enter marks of subject 1: "))
m2=int (input("enter marks of subject 2: "))
m3=int (input("enter marks of subject 3: "))
total=m1+m2+m3
average=total/3
result= "pass" if average>=40 else "fail"
print("total marks is:",total)
print("average marks is:",average)
print("result is:",result)



def calculate_bill(units):
    bill = 0
    
    if units <= 100:
       bill =  units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    elif units <= 300:
        bill = (100 * 5) + (100 *7) +(units - 200) *10

        return bill

    units = int(input("Enter electricity units consumed: "))
    print("total bill amount is: ", calculate_bill(units))



i1=int(input("enter the  initial amount: "))
print("initial amount : is,",i1)

withdraw=int(input("enter the amount to withdraw: "))
print("amount withdrawn: ", withdraw)

if withdraw < i1:
    i2 = i1 - withdraw
    print("remaining amount: ", i2)
else:
    print("insufficient funds")
    	


m1= int(input("enter the m1 marks:"))
m2= int(input("enter the m2 marks:"))
m3= int(input("enter the m3 marks:"))
total= m1+m2+m3
print (total)
average = total/3
if average >=90:
    print("grade A")
elif average >=80:
    print("grade B")
elif average >=70:
    print("grade C")
elif average >=60:
    print("grade D")
else:
    print("fail")




num = int(input("enter the value:"))
reverse = 0
while(num > 0):
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print("the reverse number is:", reverse)




num =int(input("enter a number: "))
number_of_digits = len(str(num))
print("the number of digits in the number is:", number_of_digits)
number_of_even_digits = 0
for i in str(num):
    if int(i) % 2 == 0:
        number_of_even_digits += 1
print( number_of_even_digits)
number_of_odd_digits = 0
for i in str(num):
    if int (i) % 2 != 0:
        number_of_odd_digits += 1
print( number_of_odd_digits)





num = int(input("enter a secret number: "))
guess = int(input("guess the secret number: "))

while guess != num:
    if guess < num:
        print("too low!")
    else:
        print("too high!")
    guess = int(input("guess again: "))

print("Congratulations! You guessed the number!")





product = str(input("enter a product name: "))
print(f"you entered: {product}")
quantity = int(input("enter the quantity: "))
print(f"you entered: {quantity}")
price = float (input("enter the price:"))
print(f"you entered: {price}")
total = quantity * price
print(f"the total cost is: {total}")
discount = float (input("enter discount percentage:"))
print(f"you entered: {discount}")
final_amount = total - (total * discount / 100)
print(f"the final amount is: {final_amount}")




balance = 1000   # Initial balance

while True:
    print("\n----- BANK MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance =", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 4.")





def calculate_bill(units):
    bill = 0
    
    if units <= 100:
       bill =  units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    elif units <= 300:
        bill = (100 * 5) + (100 *7) +(units - 200) *10

        return bill

    units = int(input("Enter electricity units consumed: "))
    print("total bill amount is: ", calculate_bill(units))




a=str(input("enter a number"))
reverse =str(a)[::-1]

print("the reverse is: ", reverse)
if str(a) == reverse:
    print ("it is a palindrome")
else:
    print ("it is not a palindrome")