# s1  = "Hello world"

# print (s1)

# print (len(s1))

# print ("First character: " , s1[0])

# LETS TALK ABOUT SLICING   , INDEX WILL FETCH A CHARACTER BUT SLICING WILL FETCH A SUBSTRING  

## slicing        

## understanding the syntax of slicing
#  s1[start:end:step]   ,  

# start  :   starting index at which slicing will start ,  default value is 0
# end   :   ending index at which slicing will stop ,  default value is length of string and end index is not included in the result 
# step   :   step size for slicing ,  default value is 1 stoping index ina nother word that specifies the step for slicing

S1 = "Hello world"
s1 = "Hello world"

# print(S1[2:8:1])  # slicing from index 2 to index 8 with a step of 1
# print(S1[2:9:2])  # slicing from index 2 to index 9 with a step of 2 

# slicing with default values
# print(S1[2:8])   # slicing from index 2 to index 8 with default step of 1
# print(S1[2:9:])  # slicing from index 2 to index 9 with default step of 1

s1_slice = S1[2:8:1]  # slicing from index 2 to index 8 with a step of 1 and assigning it back to s1
print(type(s1_slice))  # printing the type of s1_slice after slicing