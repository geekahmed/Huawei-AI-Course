# Solve the quadratic equation ax**2 + bx + c = 0
import cmath

coefficients = list(map(int, input("Enter coefficients: ").split()))

# calculate the discriminant
d = (coefficients[1]**2) - (4*coefficients[0]*coefficients[2])

# find two solutions
sol1 = (-coefficients[1]-cmath.sqrt(d))/(2*coefficients[0])
sol2 = (-coefficients[1]+cmath.sqrt(d))/(2*coefficients[0])

print('The solution is {0} and {1}'.format(sol1,sol2))