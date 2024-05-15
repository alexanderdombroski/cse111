"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Please enter your age: "))

min_goal = (220 - age) * .65
max_goal = (220 - age) * .85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {round(min_goal)} and {round(max_goal)} beats per minute")