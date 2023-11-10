def houseArea():
    length = float(input('what is the length of your house in feet? '))
    width = float(input('What is the width of your house in feet? '))

    area = length * width

    return area

total_area = houseArea()
print(f"\nYour house is a total of {total_area} sqft.")

from math import pi

def circumferance():
    radius = float(input('\nEnter the radius of your circle: '))

    c = 2 * pi * radius

    return c

total_circ = circumferance()
print(f"The circle has a circumferance of {total_circ}")