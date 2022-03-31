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
n=int(input("enter the number : "))
i=0
sum=0
while (i<=n):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
