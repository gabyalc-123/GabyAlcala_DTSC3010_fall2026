from scipy.stats import norm

# Question 1a and b
probability = norm.cdf(810, 750, 60) - norm.cdf(690, 750, 60)
print('Question 1a and b:')
print(f'Probability of (690 < x < 810): {probability:.4f}')
print(f'Probability of (x > 810): {norm.sf(810, 750, 60):.4f}')

# Question 2
density = norm.pdf(750, 750, 29)
print('\nQuestion 2:')
print(f'Probability density at x = 750: {density:.4f}')
