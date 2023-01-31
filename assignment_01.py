#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95 #high_score needs to be the same throughout the code. Changed the variable to match below
 
# Get the test scores.
test1 = int(input('Enter the score for test 1: ')) #Need to make these inputs integer types, if it is possible for a student to score between whole numbers then you would make this a float type
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) #Variable "test3" wasn't defined
# Calculate the average test score. 
average = (float(test1 + test2 + test3 )/3)
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
len1 = float(input("Enter a length for the 1st rectangle: "))
len2 = float(input("Enter a length for the 2nd rectangle: "))
wid1 = float(input("Enter a width for the 1st rectangle: "))
wid2 = float(input("Enter a width for the 2nd rectangle: "))

rec1=(float(len1*wid1))
rec2=(float(len2*wid2))

print('The area of the first rectangle is ', rec1, '. The area of rectangle 2 is ', rec2)
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name = str(input('Enter your preferred name: '))
age = int(input('Enter your age: '))
#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print('Happy Birthday ', name, '! You are ', age, ' years old today!')





