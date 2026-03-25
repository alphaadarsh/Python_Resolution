# count function substring from  a string 

# count function is used to count the number of occurrences of a substring in a string 
name = "python is a great language and python is easy to learn"

print(name.count("python"))  # this will count the number of occurrences of the substring "python" in the string name and print 2 because the substring "python" is present 2 times in the string name

# also 

print(f"the number of occurrences of the substring 'python' in the string name is : {name.count('python' , 0, len(name))}")  # this will print the number of occurrences of the substring "python" in the string name using f-string formatting 

#  change case of  a string  

# upeer case , lower case , title case , capitalize case  # we can convert we use to .  upper() , .lower() , .title() , .capitalize() methods to change the case of a string

# string.startswith(substring) # this method is used to check if a string starts with a specific substring or not and it returns True if the string starts with the specified substring and False otherwise