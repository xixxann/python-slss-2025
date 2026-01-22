# Files and Data

18 November 2025

## Files
For this section, we'll learn how to open and read text files.
When we open up files, we need to consider the locaton or **path** to the file.
The path to the file is where the **text file** is with respect to the **python file**. This includes information about the file's **name** and the **folder** that the file lives in.

### Opening Files
To open a file, we use the `open()` function.
The `open()` function returns a **file stream**.
Once open, the **file stream** is like a pipe that we can get information from.
```python
# information.txt is a file we want to connect to (same folder)
file = open("information.txt")
```

### Reading their contents
When reading a file stream, you receive the first part of the file first, then the second, ..., all the way to the end.
To read a part of the file steam, we use the `.readline()` method. It gives one line of information. If you call it again, you'll get the next line.
```python
# omitted code above

# read a line of text from file
line = file.readline()  		#returns string
second_line = file.readline() 	# next line
```

If you want to read all lines, you can iterate over the file stream.

```python
# omitted code aobe
# read every line until the end
for line in file:
	# do something with that line's data
	print(line)
```

### Managing File Streams
When we open a file stream, we should always close it when we finish. This helps to lower the risk of corruting any data in the file. To close a file stream, use the `.close()` method.
```python
# omitted code above
file.close() 			#closes stream safely
```

Use the `with` expression to deal with closures.
```python
with open("information.txt") as file:
	line = file.readline()
	for line in file:
		print(line) 
		# don't need to write file.close() because the with is already good

file.readline() 			# this will break
```

## Lists
Lists are a type of data that are helpful in storing more than one piece of information that is related. With lists, order matters. To create a list, we use `[]` called brackets.

```python
# To create an empty list
some_list = []
```

### Converting a String to a List
There are times where we want to get information from a string. One use case where this is applicable is the example of a `.csv` or  comma-separated values file.
```csv
Name,Age,Favourite Superhero
Mr. Ubial,67,Batman
Bruce Wayne,32,Superman
Angel Li,17,None
```

```python
# omitted code above
info = "Mr. Ubial,67,Batman"
# split the string wherever there's a ,
info_list = info.split(",") # ["Mr. Ubial", "67", "Batman"]
```

### Getting a Specific Item from a List
To access a specific element inside the list, we again use `[]` bracket notation. To get a certain thing from inside the list, we need to "know" the address, which we calll the **index**.

**indices** are always integers.

```python
# omitted code above
# index 	 -> 	0   	   1 		2
# info_list -> ["Mr. Ubial", "67", "Batman"]
# how do we access age?  ---> use index 1
print(f"Mr. Ubial's age is {info_list[1]}.")
# how do we access fave superhero? ---> -1
print(f"Mr. Ubs' favourite hero is {info_list[-1]}.")