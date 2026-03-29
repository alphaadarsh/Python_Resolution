"""List Methods

extended  
remove 
pop

"""

# extended  for adding multiple items to the list and syntax is list_name.extend(iterable)  # this will add the elements of the iterable to the end of the list and it will update the list with the new elements added at the end of the list    
fruits  =  ["apple" , "banana" , "orange"]

fruits.extend(["grape" , "kiwi"])  # adding multiple items to the list using extend method


print(len(fruits))  # printing the length of the list after extending it with new items  

# remove  for removing an item from the list and syntax is list_name.remove(item)  # this will remove the first occurrence of the item from the list and if the item is not found in the list it will raise a ValueError

fruits.remove("banana")  # removing an item from the list using remove method

# pop   

fruits.pop()  # this will remove the last item from the list and return it i can also  specify the index of the item to be removed using pop method and it will return the removed item