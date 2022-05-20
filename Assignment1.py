#ManishKumar 19105109

#Question 1
print("QUESTION-1")
a = int (input("Please Enter the First Number:"))
b = int (input("Please Enter the second number:"))
c = int (input("Please Enter the third number:"))
average=(a+b+c)/3
print("The average of three numbers is",average)

#Question 2
print("QUESTION-2")
standard_deduction=10000
additional_dependent=3000
rate=0.2
gross_income=float(input("Enter your gross income in dollars\n"))
dependents=int(input("Enter number of dependents\n"))
taxable_income=gross_income-standard_deduction-(dependents*additional_dependent)
tax=taxable_income*rate
print("Your total tax:\n",tax)

#Question 3
print("QUESTION-3")
totalSecs = int(input("Enter seconds:"))
mins = totalSecs // 60
secs = totalSecs % 60
print(mins, "minutes and", secs, "seconds")

#Question 4
print("QUESTION-4")
number_1=25
number_2="25"
number_3=25.0
number_2=int(number_1)
number_3=int(number_3)
number_4=number_1+number_2+number_3
number_4=str(number_4)
print(number_4)
print(type(number_4))

#Question 5
print("QUESTION-5")
from cmath import sin
import math
Starting_degree=0
ending_degree=345
for i in range(Starting_degree,ending_degree+1):
    if(i%15==0):

        sine_value=math.sin(math.radians(i))
        cosine_value=math.cos(math.radians(i))
        print(i," --- ",round(sine_value,4),"\t",round(cosine_value,4))

