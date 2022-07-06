#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_"+user_name.upper())

name = input("Please enter your name ")
hello_name(name)

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for i in range(1,101):
        if i%2==1:
            print(i,end=" ")

first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    return max(x for x in a_list)

print('\n',max_num_in_list([2,-4,3,2,5,13,-5]))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false).
def is_leap_year(a_year):
    return True if (a_year % 400==0 or ( a_year % 4==0 and a_year % 100!=0 )) else False

print(is_leap_year(2000))   #Leap year
print(is_leap_year(2017))   #not Leap
print(is_leap_year(1900))   #not Leap
print(is_leap_year(2016))   #Leap year


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.
def is_consecutive(a_list):
    for x in range(len(a_list)-1):
        if a_list[x] != a_list[x+1]-1:
            return False
    return True

print("consecutive --------")
print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,2,4,5]))