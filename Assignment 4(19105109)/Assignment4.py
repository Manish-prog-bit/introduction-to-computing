#QUESTION-1
print("Question-1")
entry=int(input("Enter your Marks:- "))
if entry<25:
    print("F")
elif entry<45:
    print("E")
elif entry<50:
    print("D")
elif entry<60:
    print("C")
elif entry<80:
    print("B")
else:
    print("A")
print("")
#QUESTION-2
print("Question-2")
year= int(input("Enter year: "))
if year%400==0:
    print(year,"is a Leap Year")
elif year%100==0:
    print(year,"is not a Leap Year")
elif year%4==0:
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")
print("")
#QUESTION-3
print("Question-3")

from random import randint
print("This is a multiplication game for kids")
i=1
while i<=10:
    x=randint(0, 10)
    y=randint(0, 10)
    print("Question no.",str(i),":",str(x),"X",str(y),"is")
    z=int(input("Enter your Answer:- "))
    if z==x*y:
        print("Right Answer")
    else:
        print("Wrong Answer, The answer is",x*y)
    i=i+1
print("Keep on Learning! THANK YOU!!")
print("")
#QUESTION-4
print("Question-4")
for i in range(200):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print("There are "+ str(i) +" candies in total")