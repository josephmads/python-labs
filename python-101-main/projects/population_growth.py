# Population Growth Calculator

# In the country we want to investigate:
# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

minutes_in_year = 60 * 24 * 365

pop = 380123456
births_per_min = 10
deaths_per_min = 5
immegrants_per_min = 0.667

annual_increase = ((births_per_min + immegrants_per_min - deaths_per_min) * minutes_in_year)
pop = pop + (annual_increase * 3)

print("The population will grow to", int(pop), "in the next three years.")