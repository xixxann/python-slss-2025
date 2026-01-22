# Variables, Data, Input and Output

16 September 2025

## Designing Algorithms

>A step-by-step procedure for solving a problem or accomplishing some end.
>Merriam-Webster

An algorithm is like a recipe. If you follow the steps, you should be able to solve the problem.

## Variables

We use variables to **store** values. 
Variables have two parts: a **name** and a **value**.

Example:
```python
greeting = "Hello! I am a chatbot."
```
`greeting` is the **name**.
`"Hello..."` is the **value**.

### Getting the Type

We can use the `type()` function to get the type of a variable.

`type()` is a function, just like `print()` is a *function*.

*Values*, in Python can be grouped based on their type, also known as a **data type**.

We'll look at **data types** more specifically in the next section.

### Variables names

When naming our variables, we need to follow Python's rules.

- A variable name must start with a letter or the underscore character
	- Examples:
		- myvar = "John"
		- _my_var = "John"
	- Can make variable names more variable by:
		- *Camel Case* = myVariableName
		- *Pascal Case* = MyVariableName
		- *Snake Case* = my_variable_name
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are **case-sensitive** (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.


## Data


So far, we've used two **types of data**.

`"Mr. Ubial"` is an example of a **string**.

`32` is an example of an **integer**.

`32.2` is a number, but more specifically it's an example of a **float**.

### F-String
This exists only in Python. F-string stands for **format string**. You create an f-string by putting an  `f` before the opening quotation.

```python
name = f"Mr. Ubial"
```

```python
friends_name = f"Bro"
print(f"Hey {friends_name}!")
```

You can use `{}` inside of a f-string to evaluate an expression.

## Input and Output
Whenever we want to get information from the user, we can use the `input()` function.

```python
# prompt the user for their name
# store their name in a variable

print ("What is your name?")
user_name = input()
```

command + forward slash (/) to make all the unwanted code into comments and vice verca

press cntrl c to crash the code in the terminal to stop the code from running