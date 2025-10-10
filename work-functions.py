# Functions
# Author: Angel Li
# 10 October


def create_mood_message(name: str, mood: str = "neutral") -> str:
    if mood == "happy":
        return f"Hey {name}, great to see you similing!"
    elif mood == "sad":
        return f"I hope your day gets better, {name}."
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}."
    else:
        return f"Hi {name}, hope you're having a good day."


final_message = create_mood_message("David")
print(final_message)


# Average
def average(num_one: float, num_two: float, num_three: float) -> float:
    """Return the average of three given numbers."""
    output = (num_one + num_two + num_three) / 3
    return output


output = average(94, 96, 97)
print(output)
