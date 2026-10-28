# Gaby Alcala
# Assignment 07

import numpy as np
import matplotlib.pyplot as plt

# Question 1

x = 19
y = 9

plt.plot(x,y,marker="o")
plt.show()

# Question 2

x = np.arange(1, 19)
y = -2 * x

plt.plot(x, y, "-o")
plt.show()

# Question 3

line1 = np.arange(0, 12)
line2 = line1 + line1 ** 2

plt.plot(line1)
plt.plot(line2, "o-")
plt.show()

# Question 4

datalist = [7, 2, 9, 22, 15, 6, 19, 6, 12, 12]

x = np.array(datalist)
y = x ** 2

plt.scatter(x, y, s=92)
plt.show()

# Question 5

countries = ["country1", "country2", "country3", "country4"]
gdp = [27, 4.5, 19.5, 4.6]

plt.bar(countries, gdp, width=[0.9, 0.5, 0.8, 0.6])
plt.show()

# Question 6

survey = ["q1", "q2", "q3"]
yes = [900, 340, 926]
other = [439, 619, 109]

plt.bar(survey, yes)
plt.bar(survey, other, bottom=yes)

plt.show()

# Question 7

survey = ["q1", "q2", "q3"]
yes = [600, 340, 926]
other = [439, 619, 109]

x = np.arange(len(survey))
width = 0.36

plt.bar(x - width/2, yes, width)
plt.bar(x + width/2, other, width)

plt.xticks(x, survey)
plt.show()

# Question 8

survey = ["q1", "q2", "q3"]
yes = [900, 340, 926]
other = [439, 619, 109]

plt.bar(survey, yes, label="correct")
plt.bar(survey, other, bottom=yes, label="not correct")

plt.legend(loc="upper right")
plt.title("survey results")

plt.show()

# Question 9

x = np.arange(0, 19)
y = x ** 2

plt.plot(x, y, "-o", label="squared")

plt.legend(loc="upper center")
plt.xticks(np.arange(0, 19, 2))

plt.xlabel("data")
plt.ylabel("squared")

plt.show()