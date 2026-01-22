# Numbers and Operations

5 November 2025

## Numbers, Variables, and Operations

| Name               | Python Name       | Example           |
| ---                |  ---              | ---               |
| String             |  `str`            | `"Mr. Ubial"`    |
| Boolean            |  `bool`           | `True` `False`   |
| **Integer**        |  `int`            | `1`, `-100`, `2` |
| **Float**          |  `float`          | `1.0`, `-2.3`    |

## Operators that work on Numbers

### Addition and Subtraction

```python
sum = 1 + 1                 # 2
diff = 10 - 8               # 2

some_other_sum = 1 + 1.0    # 2.0 -> will always convert to the float

````

### Multiplication and Division
```python
product = 8 * 8         # 64
dvision = 10 / 2        # 5.0
```

### Order of Operations
```python
# BEDMAS - Brackets, Exponenets, Div/Mult, Add/Sub
answer = (2 + 3) * 4 + 2 / 3
```


### Cool Other Operations
```python
# Exponents
ans = 3 ** 2 			# 9

# Floor Division
ans = 10 // 3 			# 3 -> no need to worry about decimals

# Modulo -> tells you the remainder of an operation
ans = 10 % 2 			# r0
ans = 11 % 2 			# r1
ans = 12 % 2 			# r0
ans = 13 % 2 			# r1

# Increment, decrement, multi-rement, divis-rement
egg_count = 1
egg_count += 1	     # raise the value of egg_count
egg_count -= 1		 # decrease the value of egg_count
egg_count *= 5 	 	 # multiplies value of egg_count
egg_count /= 2 	 	 # halves the value of egg_count
```

## Loops again
Recall:

```python
# Repeat something 10 times
for _ in range(10):
 print("This will be printed 10 times.")
```

Another way to loop over a *sequence*.

```python
grocery_list = [
	"cucumber",
	"eggs",
	"hot wheels",
	"tea"
]

for item in grocery_list:
	# create a bulleted list and print it out
	bulleted_item = "* " + item
	dashes = "---"
	print(bulleted_item)
	print(dashes)
```

Output:
```

* cucumbers
---
* eggs
---
* hot wheels
---
* tea
---