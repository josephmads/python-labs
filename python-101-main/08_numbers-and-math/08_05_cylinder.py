# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

from math import pi

radius = 3.14
height = 5

volume = (height * pi * (radius**2))
surface_area = (pi * (radius * 2) * (radius + height))

print(volume)
print(surface_area)