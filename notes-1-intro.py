# Notes - Introduction
# 16 September
# Angel Li

# Create our own Chatbot

# 1. Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot."

# 1a. Print the statement
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT.")
print("I'm not like the other chatbots.")
print("I'm completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8x8 is")
print("I can do it.")
print(f"8x8 is actually {8*8}.")

print("What is pi squared?")
print("I'm smart and can do it.")
print(f"It is {3.141592653 ** 2}.")

# 4. Get the name of the user and store it
user_name = input("So...what's your name? ")
print(f"It's nice to meet you, {user_name}.")

mood = input("How are you feeling today? " )
print(f"Same here, I feel {mood} as well.")

hobby = input("What is you favourite hobby? ")
print(f"That is a great choice! I like {hobby} too!")

print("Pop Quiz Time!")
answer = input("What's the fifth power of 2? ")
print(f"{answer} is a good guess. The answer is {2 ** 5}.")

if answer == "{2 ** 5}":
    print ("You are correct!")
else:
    print ("You are wrong")

print(f"It was fun talking to you {user_name}, see you soon!")

# 8. Try out branching
want_cookies = True
want_chips = False

if want_cookies and want_chips:
	print("You get both!")
else:
	print("You get none.")
