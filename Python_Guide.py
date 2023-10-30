
#This is how you print to the console 
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("----------------------------------------------------")
#Variables and Data Types
person_name = "Gavin" #String
person_age = "21" #Interger
is_male =True

print("There once was aq mane named " + person_name + ",")
print("he was " + person_age + " years old.")
print("He really liked the name" + person_name + ",")
print("but didn't like being " +person_age+ ".")

print("----------------------------------------------------")
# Getting Input from the user with String

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name)
print("Your age is " + age)
print("----------------------------------------------------") 
#Getting number
num1 = input("Enter a Number:")
num2 = input("Enter a second  Number:")
sum = float(num1) + float(num2) 
print(sum)
print("----------------------------------------------------") 
#Working With lists
friends =["Gavin", "Dustin", "Jess"]
print(friends )
print(friends[0])
print(friends[1])
print(friends[2])
# To only display Dustin and Jess we can do this 
print(friends[1:])
print("----------------------------------------------------") 
#Function
def say_hi(name1):
    print("Hello " +name1)


say_hi("Gavin")
print("----------------------------------------------------") 

# Return statment 
def cube(num):
    #The return statment will give us a value!
    return num*num*num

print(cube(3))
print("----------------------------------------------------") 
#if statment 
# and key word is both have to be true 
# or key word one could be true and the other false
def max_num(num1,num2,num3):
    # greater or equal to 
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3
    
print(max_num(3,4,5))
print("----------------------------------------------------") 

number1 = float(input("Enter first number:"))
op = input("Enter operator:")
number2 = float(input("Enter Second number:"))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
else:
    print("Invalid operator ")

print("----------------------------------------------------") 
#Dictionaries 
monthConversions ={
    "Jan": "Janurary ",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Agust",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print("----------------------------------------------------") 
#While Loop
i = 1
while i <= 10:
    print(i)
    i = i+1

print("Done the loop")
print("----------------------------------------------------") 
# Foor loop
fruit =["apple", "orange", "banana"]
for letter in "Gavin":
    print(letter)

for fruit in fruit:
    print(fruit)
# Second number will not be displayed 
    for index in range(3,10):
        print(index)
print("----------------------------------------------------") 
# Try Exceptions 
try:
    num = int(input("Enter a number:"))
except ValueError:
    print("invalid input ")
print("----------------------------------------------------") 
# Reading From outsource files
#r stand for reading 
#w stand for write
#a stand for append add (new information at the end )
gavinfile = open("Readingfile.txt", "r")
print(gavinfile.read())

gavinfile.close()
print("----------------------------------------------------") 
#Student Class 
from Student import Student 
#Object of a student class, creates a student. 
student1 = Student("Gavin", "Software Engineering", 3.1, False)
print(student1)
print(student1.name)
print("----------------------------------------------------") 
from Question import Question

questions_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:  # Convert the answer to lowercase for case-insensitive comparison
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
