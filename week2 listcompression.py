#In Python, a string can be split on a delimiter.

#Example:

#>>> a = "this is a string"
#>>> a = a.split(" ") # a is converted to a list of strings. 
#>>> print a
#['this', 'is', 'a', 'string']
#Joining a string is simple:

#>>> a = "-".join(a)
#>>> print a
#this-is-a-string 
#Task
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#Function Description

#Complete the split_and_join function in the editor below.

#split_and_join has the following parameters:

#string line: a string of space-separated words
#Returns

#string: the resulting string
def split_and_join(line):
    a=line.split(" ")
    b="-".join(a)
    return(b)
    # write your code here

if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)

#Input (stdin)
#this is a string
#Your Output (stdout)
#this-is-a-string
