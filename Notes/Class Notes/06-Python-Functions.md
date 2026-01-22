# Functions

8 October

## Function *friends*

```python
print("Hello!")
print(2.1)
```

Print is a **function** that outputs values to the console.

```python
user_information = input()
```

Waits until the user puts some information down, then returns their input.

## What is a Function

> A function is a **block of reusable code** with a **name**.

## `def`ining your own Function

```python
def <function_name>(<optional params>):
	<code bock>
```

1. Use the `def` keyword
2. Give the function a **name**
	1. convention - use lowercase and underscores
3. Write your code in an **indented code block**

## Calling a **Function**

```python
<function_name>(<optional args>)
```

When we use a function, we say we **call** it.
We call a function by using its name followed by parentheses. If there are any value that we need, we put them in the parentheses.

```python
def say_hello_nicely(name: str):
	print(f"hello {name}!")

say_hello_nicely("steve")
```

We use functions to help us save time/keystrokes.

```python
def normalize_input(user_input: str):
	"""Takes user input and cleans it up."""
	output = user_input.lower().stripe(",.?!")
	return output
```
## Parameters

**Parameters** are the **inputs** of the function.

```python
# Create a function that represents f(x) = x^2
def squared(num: float):
	output = num ** 2
	print(output)

def power(num: float, exp: float):
	"""Raise a number to a power."""
	output = num ** exp
	print(output)

squared(2)      #4
squared(2.2)    # 2.2 * 2.2
power(2, 2)     # 4
power(3.5, 2.2) # ???
```

## `return` values

The **return** keyword is used to give the function an **output value**. In a functon, the `return` keyword will stop the execution of the rest of the function.

```python
def some_fun():
	print("hello!")

def some_fun_return() -> str:
	print("hello!")
	return "hello!"

return_val = some_fun()

print(return_val) # value is None

return_val = some_fun_return()

print(return_val) # value is hello!
```

## Default Arguments

**Parameters** are the *inputs* to a function.
**Arguments** are the *values* given as inputs.

```python
# our example from notes-3-functions.py
def say_hello_nicely(name="Skip"):
	print(f"hello {name}")

say_hello_nicely("David") # David is the argument
say_hello_nicely()
```