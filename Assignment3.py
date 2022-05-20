#ManishKumar 19105109
#Question 1
print("QUESTION-1")
Number=int(input("Enter a number:"))
Num_bin=[]
while(Number>0):
    Bin_digit=Number%2
    Num_bin.append(Bin_digit)
    Number=Number//2
Num_bin.reverse()
print("Binary Equivalent is:")    
for i in Num_bin:
    print(i,end="  ")

#Question 2
print("Question-2")
print('''Welcome to the calculator. Please choose the operation
      1 - Addition
      2 - Subtraction
      3 - Multiplication
      4 - Division''')
operation = int(input("operation operations form 1, 2, 3, 4:"))   
number_1=int(input("Enter first number:"))
number_2 = int(input("Enter second number:")) 
if operation ==1:
    print(number_1,"+", number_2,"=", number_1+number_2)  
elif operation ==2:
    print(number_1,"-", number_2,"=", number_1-number_2) 
elif operation ==3:
    print(number_1,"*", number_2,"=", number_1*number_2)  
if operation ==4:
    print(number_1,"/", number_2,"=", number_1/number_2)  
else:
    print("Invalid input")


#Question 3
print("Question-3")
#A
print("Answer-A")
print((3+4)*5)

#B
print("Answer-B")
number=float(input("Enter your number:-\n"))
print((number)*(number-1)/2)

#C
print("Answer-C")
number_2=float(input("Enter the value of radius:\n"))
print(4*3.14*number_2*number_2)

#D
print("Answer-D")
import math
import cmath
angle1=float(input("Enter the value of alpha in degrees:\n"))
angle2=float(input("Enter the value of beta in degrees:\n"))
number_3=float(input("Enter the value of r\n"))
p=((number_3*cmath.cos(angle1)))**2
q=((number_3*cmath.sin(angle2)))**2
r=p+q
print(cmath.sqrt(r))

#E
print("Answer-E")
number_4=float(input("Enter the value of x1:\n"))
number_5=float(input("Enter the value of y1:\n"))
number_6=float(input("Enter the value of x2:\n"))
number_7=float(input("Enter the value of y2:\n"))
c=number_7-number_5
v=number_6-number_4
print("Final Answer :- ",c/v)

#Question 4
print("Question-4")
print("Printing different ranges")
print("Answer-A")
for i in range(5):
    print(i)
    print("")
print("Answer-B")
for i in range(3,10):
        print(i)
        print("")
print("Answer-C")
for i in range(4,13,3):
        print(i)
        print("")
print("Answer-D")
for i in range(15,5,-2):
        print(i)
        print("")
print("Answer-E")
for i in range(5,3):
        print(i)
        print("")

#Question 5
print("Question-5")
num_h=int(input("Enter number of hydrogen atoms :- "))
num_c=int(input("Enter number of carbon atoms :- "))
num_o=int(input("Enter number of oxygen atoms :- "))

mass_c=12.0107
mass_h=1.00794
mass_o=15.9994

mass_molecule=(num_h*mass_h)+(num_c*mass_c)+(num_o*mass_o)

print('Mass Molecule is :-',mass_molecule)

