"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
text = open('foo.txt')
print(text.read())
text.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
write_text = open('bar.txt', 'w')
write_text.write('This is line one.\n')
write_text.write('This is line two.\n')
write_text.write('This is line three.\n')
write_text.close()

read_text = open('bar.txt')
print(read_text.read())
read_text.close()
