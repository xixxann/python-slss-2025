# Branching
23 September
## `if`
Branching is a concept in compter science that allows us to write code that has  *two or more dfferent outcomes*.
This is the "grammar" of the `if` expression.
```python
if <statement>: 
	<code block - line 1>
	<...>
	<code block - line n>

```

Example:
```python
user_name = "Mr. Ubial"
if user_name == "Mr. Ubial":
	print("Access granted.")
	print("You can see all the secret information.")
```

## `elif` and `else`

`elif` and `else` are keywords we can use to extend our `if` expressions.
If we want to add *more* branches, we use these keywords.
`elif` is short for **else if**.

```python
user_name = "Mr. Ubial"
if user_name == "Mr. Ubial":
	print("Access granted.")
	print("You can see all the secret information.")
elif user_name == "Spongebob":
	print("🎶 Who lives in a pineapple under the sea? 🎶")
	print("Spongebob Squarepants!")
elif user_name == "Abraham Lincoln":
	print ("Abe Lincoln? I heard you're a good wrestler.")
else: 
	print("I don't have any secrets for you.")
```

## Booleans
> Asking my Computer Science nerd friends.
> "Do you want pizza OR burgers?"
> They replied:
> "YES!"

**Booleans** are a type of data in Python. Booleans are binary and are either `True` or `False`.

```python
is_sunny = True

if is_sunny:
	print("Bring your sunscreen.")
else:
	print("Bring a sweater?")
```

### `or`
`or` can be used to join two or more statements together.
An `or` expression is `True` if and only if at least one statement is `True`
```python
want_burgers = True
want_pizza = True

if want_burgers or want_pizza:
	print ("YES") # this is going to print
else:
	print ("NO")
```

### `and`
An `and` expression is `True` if and only if **both** statements are `True`.

```python
want_cookies = True
want_chips = False

if want_cookies and want_chips:
	print("You get both!")
else:
	print("You get none.") # this will print
```