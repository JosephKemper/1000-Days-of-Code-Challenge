# 01 Checkpoint: Review Python Assignment

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
# Get the user's age as an integer.
user_age = int(input ("Please enter your age: "))

# Compute the slowest and fastest benificial heart rates from the user's age
max_heart_rate = 220 - user_age
upper_range = max_heart_rate * 0.85
lower_range = max_heart_rate * 0.65

# Blank line for asthetics
print ()

# Display results to the user. 
print (f"""When you exercise to strengthen your heart, you should 
keep your heart rate between {lower_range:.0f} and {upper_range:.0f} beats per minute.""")


