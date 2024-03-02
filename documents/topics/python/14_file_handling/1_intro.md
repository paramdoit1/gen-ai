# File Handling in Python
## Introduction:
Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, like other concepts of Python, this concept here is also easy and short. 
Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters, and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with the reading and writing files. 

## Python File Open
Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

```
f = open(filename, mode)
```

Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

## Working in Read mode

Example 1: The open command will open the Python file in the read mode and the for loop will print each line present in the file.

```
# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')

# This will print every line one by one in the file
for each in file:
	print (each)

```

```
Output:

Hello world
GeeksforGeeks
123 456

```
Example 2: In this example, we will extract a string that contains all characters in the Python file then we can use file.read(). 

```
# Python code to illustrate read() mode
file = open("geeks.txt", "r") 
print (file.read())

# Output:

Hello world
GeeksforGeeks
123 456

```

Example 3: In this example, we will see how we can read a file using the with statement in Python.

```
   
# Python code to illustrate with()
with open("geeks.txt") as file:  
    data = file.read() 
 
print(data)
# Output:

Hello world
GeeksforGeeks
123 456
```

Example 4: Another way to read a file is to call a certain number of characters like in the following code the interpreter will read the first five characters of stored data and return it as a string: 

```

file = open("geeks.txt", "r")
print (file.read(5))
# Output:

Hello
```
Example 5: We can also split lines while reading files in Python. The split() function splits the variable when space is encountered. You can also split using any characters as you wish.

```
# Python code to illustrate split() function
with open("geeks.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
# Output:

['Hello', 'world']
['GeeksforGeeks']
['123', '456']
```

## Creating a File using the write() Function
Just like reading a file in Python, there are a number of ways to Writing to file in Python. Let us see how we can write the content of a file using the write() function in Python.

Let’s see how to create a file and how the write mode works.

Example 1: In this example, we will see how the write mode and the write() function is used to write in a file. The close() command terminates all the resources in use and frees the system of this particular program. 

```  
# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# Output:

This is the write commandIt allows us to write in a particular file

```
Example 2: We can also use the written statement along with the  with() function.

```
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f: 
	f.write("Hello World!!!")

```
```
Output:

Hello World!!!

```

## Working of Append Mode
Let us see how the append mode works.

Example: For this example, we will use the Python file created in the previous example.

```
# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

```
```
Output:

This is the write commandIt allows us to write in a particular fileThis will add this line
```

## Implementing all the functions in File Handling

```
import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)

````

```
Output:

File example.txt created successfully.
Hello, world!
Text appended to file example.txt successfully.
Hello, world!
This is some additional text.
File example.txt renamed to new_example.txt successfully.
Hello, world!
This is some additional text.
File new_example.txt deleted successfully.
```