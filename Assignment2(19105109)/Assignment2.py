#ManishKumar 19105109
#Question 1
print("QUESTION-1")

str = "Python is a case sensitive language"
print(len(str))
txt = "Python is a case sensitive language"[::-1]
print(txt)
s1 = slice(9,26)
print(str[s1])
x=str.replace("a case sensitive","object oriented")
print(x)
print(str.find("a"))
str2=str.replace(' ','')
print (str2)

#Question 2
print("QUESTION-2")

name='Manish Kumar'
print(f"Hey,{name} here.")

SID='19105109'
print(f"My SID is {SID}.")

Branch='ECE'
CGPA='9.9'
print(f"I am from {Branch} department and my CGPA is {CGPA}.")

#Question 3
print("QUESTION-3")
a=56
b=10
print(a)
print(b)
#Print bitwise AND operation
print("a&b=",a&b)
#Print bitwise OR operation
print("a|b=",a|b)
#Print bitwise XOR operation
print("a^b=",a^b)
#Print bitwise right shift operation
print("a>>2=",a>>2)
print("b>>4=",b>>4)
#Print bitwise left shift operation
print("a<<2=",a<<2)
print("b<<2=",b<<2)

#Question 4
print("QUESTION-4")
a=input("Enter any word:- ")
b=("name")
if(a.find(b)==-1):
    print("NO")
else:
    print("YES") 
print("")

# QUESTION NO.5
print("QUESTION-5")
print("Enter first side of triangle:-")
side1=int(input())
print("Enter second side of triangle:-")
side2=int(input())
print("Enter third side of triangle:-")
side3=int(input())

A=side1<side2+side3
B=side2<side1+side3
C=side3<side2+side1

Result= str(A&B&C)
print("The sides entered by user can form a triangle?")
Result=Result.replace("True","YES")
Result=Result.replace("False","NO")
print("The Answer is ",Result)
print("")

# QUESTION NO.6
print("QUESTION-6")
a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
c=(a^b)
d=bin(c)
count=0
for i in d[2:]:
    if i=="1":
        count+=1
    print(count)   