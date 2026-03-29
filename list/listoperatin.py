# reverse ,  sort , count  , Membership op , index 

days_of_week = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"] 
print (days_of_week)  # printing the original list of days of the week

#reverse  for reversing the order of the items in the list and syntax is list_name.reverse()  # this will reverse the order of the items in the list and it will update the list with the reversed order of items
days_of_week.reverse()  # reversing the order of the items in the list using reverse method
print(days_of_week)  # printing the reversed list of days of the week
 
# sort  for sorting the items in the list in ascending order and syntax is list_name.sort()  # this will sort the items in the list in ascending order and it will update the list with the sorted order of items
numbers = [5 , 2 , 9 , 1 , 3]
numbers.sort(reverse=True)  # sorting the items in the list using sort method
print(numbers)  # printing the sorted list of numbers

# count  for counting the number of occurrences of an item in the list and syntax is list_name.count(item)  # this will return the number of occurrences of the item in the list
fruits = ["apple" , "banana" , "orange" , "apple" , "grape"]
print(fruits.count("apple"))  # counting the number of occurrences of "apple" in
# the list of fruits using count method

# membership operator  for checking if an item is present in the list or not and syntax is item in list_name  # this will return True if the item is present in the list and False if the item is not present in the list
print("banana" in fruits)  # checking if "banana" is present in the list
print("kiwi" in fruits)  # checking if "kiwi" is present in the list

