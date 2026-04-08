# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
  sum = sum + (temp % 10)
  temp = int(temp / 10)
print(f"Sum of digits of {num} = {sum}")
