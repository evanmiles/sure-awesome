#progressTracker.py

# A program for calculating percent complete

from __future__ import division

# Ask the user how many assignments they have completed

numAss = eval(input("Enter the number assignments you've completed so far: "))

# Ask the user how many days they've been enrolled in the course

numDays = eval(input("Enter the number of days you've been enrolled in the course: "))

# Convert days to hours enrolled (one day being equal to three hours average work)

print ("{:.0%}".format(numAss/numDays))

