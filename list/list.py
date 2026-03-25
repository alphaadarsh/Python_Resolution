# list is a collection of data type  you can store multiple values in a list and it is ordered and mutable data type in python 

# creating a list in python  

st_data = ["Jhon" , 20 , 85.5 ]
print(type(st_data))  # this will print the type of st_data which is <class 'list'> because st_data is a list in python
print(st_data)  # this will print the list st_data which contains the name, age and percentage of a student itcan contain in any data types as allowed in elements of a list in python  in a ordered manner and it is mutable data type in python which means we can change the values of the list after creating it


#  list is  same as indexing and slicing in string but the only difference is that list is mutable data type in python which means we can change the values of the list after creating it but string is immutable data type in python which means we cannot change the values of the string after creating it  

day_in_week = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "sunday"]
print(day_in_week)  # this will print the list day_in_week which contains the names
print(day_in_week[2])  # this will print the list day_in_week which contains the names  


# length of the list  

print(len(day_in_week))  # this will print the length of the list day_in_week which is 7 because there are 7 elements in the list day_in_week which are the names of the days in a week  

print(f"The length of the list day_in_week is {len(day_in_week)}")  # this will print the length of the list day_in_week which is 7 because there are 7 elements in the list day_in_week which are the names of the days in a week using f string in python to print the length of the list day_in_week in a formatted way 

# slicing in list is same as slicing in string but the only difference is that list is mutable data type in python which means we can change the values of the list after creating it but string is immutable data type in python which means we cannot change the values of the string after creating it 

print(day_in_week[2:5])  # this will print the list day_in_week which contains the names of the days in a week from index 2 to index 4 because the end index is not included in the result of slicing in python and it will print ['wednesday', 'thursday', 'friday'] which are the names of the days in a week from index 2 to index 4 in the list day_in_week

l1 = [1, 2, 3, 4, 5,6,7,8,9,10]

print (l1[1:9:2])  # this will print the list l1 which contains the numbers from index 1 to index 8 with a step of 2 because the end index is not included in the result of slicing in python and it will print [2, 4, 6, 8] which are the numbers from index 1 to index 8 with a step of 2 in the list l1


# concatination of list is same as concatenation of string but the only difference is that list is mutable data type in python which means we can change the values of the list after creating it but string is immutable data type in python which means we cannot change the values of the string after creating it

la1 = [1, 2, 3]
la2 = [4, 5, 6]

print(la1 + la2)  # this will print the concatenation of the list la1 and la2 which is [1, 2, 3, 4, 5, 6] because the + operator is used to concatenate two lists in python and it will print the concatenation of the list la1 and la2 which is [1, 2, 3, 4, 5, 6] because the + operator is used to concatenate two lists in python and it will print the concatenation of the list la1 and la2 which is [1, 2, 3, 4, 5, 6] because the + operator is used to concatenate two lists in python and it will print the concatenation of the list la1 and la2 which is [1, 2, 3, 4, 5, 6] because the + operator is used to concatenate two lists in python and it will print the 

# repetation  of list is same as repetition of string but the only difference is that list is mutable data type in python which means we can change the values of the list after creating it but string is immutable data type in python which means we cannot change the values of the string after creating it


la3 = [1, 2, 3]
la4 = [4, 5, 6]  

print(la3 * 3 )  # this will print the repetition of the list la3 which is [1, 2, 3, 1, 2, 3, 1, 2, 3] because the * operator is used to repeat a list in python and 

# append on the list  #synatax 
# list_name.append(element)  # this will append the element at the end of the list  in append list willl get updated with the new element added at the end of the list
# this is called mutabilty 

fruits  = ["apple" , "banana" , "orange"]

fruits.append("grapes")  # this will append the element "grapes" at the end of the list fruits and it will update the list fruits with the new element added at the end of the list fruits which is "grapes"

print(fruits)  # this will print the list fruits which contains the names of the fruits in a list and it will print ['apple', 'banana', 'orange', 'grapes'] because the append method is used to append the element "grapes" at the end of the list fruits and it will update the list fruits with the new element added at the end of the list fruits which is "grapes" 

# insert method in list  # syntax 
# list_name.insert(index , element)  # this will insert the element at the specified index in the list and it will update the list with the new element added at the specified index in the list

fruits.insert(1 , "kiwi")  # this will insert the element "kiwi" at index 1 in the list fruits and it will update the list fruits with the new element added at index 1 in the list fruits which is "kiwi"
print(fruits)  # this will print the list fruits which contains the names of the fruits in a list and it will print ['apple', 'kiwi', 'banana', 'orange', 'grapes'] because the insert method is used to insert the element "kiwi" at index 1 in the list fruits and it will update the list fruits with the new element added at index 1 in the list fruits which is "kiwi" 