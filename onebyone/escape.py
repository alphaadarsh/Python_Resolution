# starts with  \ 
# \n , \t , \r , \b , \f , \v , \\ , \',    are called escape sequence characters

print("hello\nworld")  # this will print hello and world in two different lines because of \n escape sequence character  

print("hello\tworld")  # this will print hello and world in the same line with a tab space in between because of \t escape sequence character

print("hello\rworld")  # this will print world and hello in the same line because

# \r escape sequence character will move the cursor to the beginning of the line and overwrite the existing characters
print("hello\bworld")  # this will print helloworld because \b escape sequence character

# will move the cursor back by one position and overwrite the existing character
print("hello\fworld")  # this will print hello and world in two different lines because

# \f escape sequence character will move the cursor to the next line and start printing from there
print("hello\vworld")  # this will print hello and world in two different lines because
# \v escape sequence character will move the cursor to the next line and start printing from there
print("hello\\world")  # this will print hello\world because \\ escape sequence character will print a single backslash
print("hello\'world")  # this will print hello'world because \' escape sequence character
# will print a single quote
print("hello\"world")  # this will print hello"world because \" escape sequence character
# will print a double quote