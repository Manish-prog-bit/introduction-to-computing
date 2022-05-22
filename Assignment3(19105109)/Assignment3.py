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
print("")

#Question 2
print("QUESTION-2")
print("This is an Python calculator program.")
n = input("Enter the expression by using these operations (+,-,*,/,**,//,%) :-")
print("Your answer is equal to :- ",end=" ")
print(eval(n))
print("")

#Question 3
print("QUESTION-3")
#A
print("Answer-A")
print((3+4)*5)

#B
print("Answer-B")
number=float(input("Enter the value of n:-\n"))
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
print("QUESTION-4")
print("Printing different ranges")
print("Answer-A")
for i in range(5):
    print(i)
print("Answer-B")
for i in range(3,10):
        print(i)
print("Answer-C")
for i in range(4,13,3):
        print(i)
print("Answer-D")
for i in range(15,5,-2):
        print(i)
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

