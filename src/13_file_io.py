"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open("foo.txt", "r")
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

import os
if (os.path.exists("bar.txt")):
    os.remove("bar.txt")

b = open("bar.txt", "w")
b.write("first line\n")
b.write("second line\n")
b.write("third line")
b.close()

b = open("bar.txt", "r")
print(b.read())
b.close()