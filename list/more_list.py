"""List Methods

extended  
remove 
pop

"""

# extended  for adding multiple items to the list and syntax is list_name.extend(iterable)  # this will add the elements of the iterable to the end of the list and it will update the list with the new elements added at the end of the list    
fruits  =  ["apple" , "banana" , "orange"]

fruits.extend(["grape" , "kiwi"])  # adding multiple items to the list using extend method


print(len(fruits))  # printing the length of the list after extending it with new items