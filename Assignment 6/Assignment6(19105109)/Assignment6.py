#ASSIGNMENT-6
#QUESTION-1
# Python program to check perfect number using function

def perfect_numbers(N):  #user-defined function
   sum = 0
   for i in range(1,N):
      if(N%i == 0):
         sum = sum+i
   return sum

# take inputs
N = int(input("Enter a number: "))

# check perfect number or not
if(N == perfect_numbers(N)):
   print(N, "is a Perfect number")
else:
   print(N, "is not a Perfect number")
print("")

#QUESTION-2
def isPalindrome(s):  # user-defined function
    s = s.lower()
    length = len(s)

    if length < 2:
        return True

    elif s[0] == s[length - 1]:
        # Call is pallindrome form substring(1,length-1)
        return isPalindrome(s[1: length - 1])

    else:
        return False


# take inputs
string = input('Enter the string: ')

# calling function and display result
reverse = isPalindrome(string)
if reverse:
    print(string, 'is a Palindrome')
else:
    print(string, 'is not a Palindrome')
print("")

#QUESTION-3
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
n = int(input("Enter number of rows:- "))
pascal_triangle(n)
print("")

#QUESTION-4
#importing string module
import string
## function to check for the panagram
def is_panagram(string, alphabets):
   ## looping over the alphabets
   for char in alphabets:
      ## if char is not present in string
      if char not in string.lower():
         ## returning false
         return False
   return True
## initializing alphabets variable
alphabets = string.ascii_lowercase
## initializing strings
string = "The Quick Brown Fox Jumps Over The Lazy Dog"
print("The String is a Panagram") if is_panagram(string, alphabets) else print("The Not Panagram")
print("")

#QUESTION-5
# Give the hyphen-separated string as user input using the input() function.
givn_strng = input('Enter some random string = ')
# print the string before modification
print('The string before modification = ', givn_strng)
# Split the hyphen-separated strings into a list of strings using the split()
# function and store it in a variable.
wordsLis = givn_strng.split('-')
# sort the given list using the sort() function.
wordsLis.sort()
# Print the sorted sequence by joining the words in the list with a hyphen.
resultwords = '-'.join(wordsLis)
# print the resultwords
print('The string after modification = ', resultwords)
print("")

#QUESTION-6
def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Manish Kumar","ECE",19105109)
print("")

#QUESTION-7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()
print("")

#QUESTION-8
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
print("")

#QUESTION-9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str

s = input("Enter the parantheses you want to check : ")
if parantheses.find(s):
    print(s,"-","are valid")
else:
    print(s,"-","are invalid")
