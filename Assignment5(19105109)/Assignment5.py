#Assignment 5
#QUESTION-1
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = input("Enter A String: ")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
print("")
#QUESTION-2
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
print("")
#QUESTION-3
import random

i=0
while i<5:
    s1 = int(input("Enter your first side:-"))
    s2 = int(input("Enter your second side:-"))
    s3 = int(input("Enter your third side:-"))
    s = (s1 + s2 + s3) / 2
    if s1+s2>s3 and s3+s2>s1 and s1+s3>s3 :
        print("Area is equal to :-",(s*(s-s1)*(s-s2)*(s-s3))**(1/2))
    else :
        print("The sides entered don't for a triangle!!!")
    i=i+1
print("you were having only 5 turns to enter the sides of your triangle!!")

print("")
#QUESTION-4
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# Question 5
x = int(input("Enter the number of rows: "))
y = 65
for i in range(1,x+1):
    for j in range(0,i):
            z = chr(y)
            print(z, end="")
            y += 1
            if (y-65)%26==0:
                y=65
    print("")

print("")


#QUESTION-6
# First, we will take the input:
lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range ",lower_value,"and",upper_value,"are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

#QUESTION-7
nl=[]
for x in range(1, 500):
    if (x%7==0) and (x%11==0):
        nl.append(str(x))
print ("The numbers which are multiple of 7 and divisible by 11 are :",(nl))


# Question No.8
print("Enter 10 integers of your choice")
nl = []
i=1
while i<11:

    num1=int(input("Enter an integer-:"))
    nl.append(num1)
    i=i+1


print("list of integers entered by the user-:", nl)
print("Positive numbers are as follows-:",end="")
for i in nl:
    if i>0:
        print(i,end=",")
print("\nNegative numbers are as follows-:",end="")
for i in nl:
    if i<0:
        print(i,end=",")
print("\nOdd numbers are as follows-:",end="")
for i in nl:
    if (i%2!=0)&(i>0):
        print(i,end=",")
print("\nEven numbers are as follows-:",end="")
for i in nl:
    if (i%2==0)&(i>0):
        print(i,end=",")
count1=int(input("\nEnter the number you want to count in list-:"))
count_num=nl.count(count1)
print("The number -",count1,",","occurs",count_num,"times in the list")

print("")

# Question No.9
print("Enter 10 words in list")
nl=[]
for item in range(10):
    words=input("The word you want to add in the list-:")
    nl.append(words)

count1=input("Enter the word you want to count in list-:")
count_list=nl.count(count1)
print("word -",count1,",","occurs",count_list,"times")
