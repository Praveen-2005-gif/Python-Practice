# print hello world
print("Hello,World!")

# print your name
name=input("Enter your name:")
print("Hello ",name)

# add two numbers
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=a+b
print("Sum=",c)

# area of rectangle
l=float(input("Enter the length:"))
b=float(input("Enter the breadth:"))
area=l*b
print("Area of rectangle=",area)

# celsius to fahrenit
celsius=float(input("Enter temperature in celsius:"))
fahrenit=(celsius*9/5)+32
print("Temperature in fahrenit:",fahrenit)

# check if number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("odd")

# factorial of a number
num=int(input("Enter a number:"))
fact=1
for i in range(1, num+1):
    fact=fact*i
print("Factorial of a number=",fact)

# largest of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>=num2 and num1>=num3:
    print("Largest number=",num1)
elif num2>=num1 and num2>=num3:
    print("Largest number=",num2)
else:
    print("Largest number=",num3)

# swap of two numbers using temp variable
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
temp=num1
num1=num2
num2=temp
print("After swapping:")
print("num1=",num1)
print("num2=",num2)

# without using temp variable
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1,num2=num2,num1
print("After swapping:")
print("num1=",num1)
print("num2=",num2)

