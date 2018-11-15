# Our new calculator is censored and as such it does not accept certain words. 
# You should try to trick by writing a program to calculate the sum of numbers.
# Given a list of numbers, you should find the sum of these numbers. 
# Your solution should not contain any of the banned words, even as a part of another word.
# The list of banned words are as follows :
# sum
# import
# for
# while
# reduce

# Input: A list of numbers.
# Output: The sum of numbers.
# ** Example :
# ** checkio([1, 2, 3]) == 6
# ** checkio([2, 2, 2, 2, 2, 2]) == 12
# Precondition: The small amount of data. Let's creativity win!
# How it is used: This task challenges your creativity to come up with a solution to fit this mission's specs!

def fn(List, total):

    if len(List) > 0 :
        total = total + List[0]
        result = fn(List[1:], total)
        return result
    else :
        return total

def checkio(data):     
    return fn(data,0)