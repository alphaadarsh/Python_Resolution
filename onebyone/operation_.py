s1  =  "python is a great language"

# print (s1)
print(s1*3) # this will print the string s1 three times in a row without any space in between

# membership operator in python is used to check if a substring is present in a string or not

s2 = "python is fun"
print("python" in s2)  # this will return True because the substring "python" is present in the string s2
print("java" in s2)  # this will return False because the substring "java

# comparision of string in python is done using the ascii values of the characters in the string
print("python" > "java")  # this will return True because the ascii value of 'p' is greater than the ascii value of 'j'
print("python" < "java")  # this will return False because the ascii value
print("python" == "Python")  # this will return False because the ascii value of 'p' is not equal to the ascii value of 'P' 

# strips use for removing the leading and trailing whitespace characters from a string
s3 = "   python is a great language   "
print(s3.strip())  # this will remove the leading and trailing whitespace characters from the string s3 and print "python is a great language" without any leading or trailing whitespace characters

# replace method in python is used to replace a substring with another substring in a string

s4 = "python is a great language"
print(s4.replace("python", "java"))  # this will replace the substring "python   we can also add count to 1 that on;ly the first occurrence of "python" will be replaced with "java" in the string s4 and print "java is a great language" if we want to change n number of occurrences of "python" to "java" then we can add count to n in the replace method like this s4.replace("python", "java", n) where n is the number of occurrences we want to replace

#  //  this si called floor division operator in python and it is used to divide two numbers and return the quotient as an integer by discarding the decimal part of the result 