def houseArea():
    length = float(input('what is the length of your house in feet? '))
    width = float(input('What is the width of your house in feet? '))

    area = length * width
    # print(f"\nYour house is a total of {area} sqft.")
    return f"\nYour house is a total of {area} sqft."



from math import pi

def circumferance():
    radius = float(input('\nEnter the radius of your circle: '))

    c = 2 * pi * radius
    # print(f"\nThe circle has a circumferance of {c}")
    return f"\nThe circle has a circumferance of {c}"

