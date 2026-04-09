# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
score = int(input("Enter your score: "))
if score > 89 and score < 101:
  print("Grade: A")
elif score > 79:
  print("Grade: B")
elif score > 69:
  print("Grade: C")
elif score > 59:
  print("Grade: D")
elif score < 60 and score > 0:
  print("Grade: F")
else:
  print("Invalid score")
