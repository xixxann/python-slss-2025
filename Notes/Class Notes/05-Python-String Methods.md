# (String) Methods

## Slide Deck
[3 - String Methods.pdf](../../_resources/3%20-%20String%20Methods.pdf)

## `in` keyword --> `str`

If you want to see if a string contans some characters or if it contains a **substring** we can use the `in` keyword.

```python

# Ask the customer if they want fries
fries_reply = input("Do you want fries?")
# "yes!"
# "Yes!"

if "yes" in fries_reply.lower():
	print("Here are your fries.")
else:
	print("OK, you will not have fries.")

```