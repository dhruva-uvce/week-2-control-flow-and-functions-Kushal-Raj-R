
# Q09. Functions with Default Parameters
#
# Write the following two functions:
#
#   greet(name, greeting="Hello")
#       Returns the string: "{greeting}, {name}!"
#
#   power(base, exp=2)
#       Returns base raised to exp.
#
# Then in the main block below, call and print:
#   greet("Alice")          → "Hello, Alice!"
#   greet("Bob", "Hi")      → "Hi, Bob!"
#   power(5)                → 25
#   power(2, 10)            → 1024


def greet(name, greeting="Hello"):
    # --- YOUR CODE HERE ---
    print(greeting + ", " + name + "!")


def power(base, exp=2):
    # --- YOUR CODE HERE ---
    print(base ** exp)


if __name__ == "__main__":
    # Call the functions and print results
    # --- YOUR CODE HERE ---
    greet("Alice")
    greet("Bob", "Hi")
    power(5)
    power(2,10)
