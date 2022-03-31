# Given an integer n, find if n is positive, negative or 0.
# If n is positive, print "Positive"
# If n is negative, print "Negative"
# And if n is equal to 0, print "Zero" 
  
# n=int(input("enter the number:"))
# if n>0:
#     print("positive number ")
# elif n<0:
#     print("negative number")
# else :
#     print("number is zero")
 
#  Given an integer n, find and print the sum of numbers from 1 to n

# n=int(input("enter the number : "))
# sum=0
# i=0
# while (i<=n):
#     sum=sum+i
#     i=i+1
# print(sum)

# Given a number N, print sum of all even numbers from 1 to N.


# n=int(input("enter the number : "))
# i=0
# sum=0
# while (i<=n):
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)

# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

# s=int(input("enter the starting fahrenheit temperature:"))
# e=int(input("enter the end  fahrenheit temperature:"))
# w=int(input("steps taken :"))
# while s<=e:
#     c=(s-32)*5//9
#     print(s,c)
#     s=s+w

# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
 
# while True :
#     n = int(input())
#     if n==1:
#         a = int(input())
#         b = int(input())
#         print(a+b)
#     elif n==2:
#         a = int(input())
#         b = int(input())
#         print(a-b)
#     elif n==3:
#         a = int(input())
#         b = int(input())
#         print(a*b)
#     elif n==4:
#         a = int(input())
#         b = int(input())
#         print(a//b)
#     elif n==5:
#         a = int(input())
#         b = int(input())
#         print(a%b)
#     elif n==6:
#         break
#     else:
#         print("Invalid Operation")


# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

# res=input("enter the number")[::-1]
# res=res.lstrip("0")
# print(res)


