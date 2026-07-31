# Positive, negative, or zero
num=int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

# Print 1-10 using for
for i in range(1, 11):
    print(i)

# Print 1-10 using while
i=1
while i<=10:
    print(i)
    i+=1

# Multiplication table
num=int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# Sum of first N numbers
n=int(input("Enter a number: "))
total=0
for i in range(1, n+1):
    total+=i
print("Sum =", total)

# Reverse a number
num=int(input("Enter a number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num // 10
print("Reversed number =", rev)

# Pattern program
for i in range(1, 6):
    print("*" * i)

# Palindrome
num=int(input("Enter a number: "))
temp=num
rev=0

while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp //10
if num==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# prime number
num=int(input("Enter a number: "))
if num<=1:
    print("Not prime")
else:
    for i in range(2,int(num **0.5)+1):
        if num% i==0:
            print("Not prime")
            break
    else:
        print("Prime")

# Leap year
year=int(input("Enter a year: "))
if (year%400==0) or(year % 4==0 and year %100!=0):
    print("Leap year")
else:
    print("Not a leap year")

# Fibonacci series
n=int(input("Enter number of terms: "))
a=0
b=1
print("Fibonacci Series: ")
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
