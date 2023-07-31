'''
-ask for name
-ask for age

-print message that tells them 
 the year that they will turn 100 years old
'''
print("name: ")
name = input()

print("age: ")
age = int(input())

currentYear = 2023
year = (100 - age) + currentYear
print(name + " the year you will turn 100 is " + str(year))