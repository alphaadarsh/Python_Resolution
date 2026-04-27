# strings always take extra space  
# they are immutable, so every time we change them, a new string is created in memory every string has there own unicode mapping and they are indexed and sliced same as list but the only difference is that string is immutable data type in python which means we cannot change the values of the string after creating it but list is mutable data type in python which means we can change the values of the list after creating it

# A  = "Hello World" 
# TYPE  CONVERSION IN STRING

# 1. int to string
num = 123  
# str_num = str(num)
a = str(num)  # Convert integer to string
print(a)  # Output: '123'

print(type(a))  # Output: <class 'str'>

# there are falsy and truthy values in python, empty string is falsy value and non-empty string is truthy value
# falsy values in python are 0, 0.0, 0j, Decimal(0), Fraction(0, 1), None, False, empty sequences and collections (e.g., '', (), [], {})
# truthy values in python are all values that are not falsy, including non-empty strings, non-zero numbers, non-empty sequences and collections, and custom objects that do not define a __bool__() or __len__() method that returns 0 or False.

# implicit type conversion in string and explicit type conversion in string
  