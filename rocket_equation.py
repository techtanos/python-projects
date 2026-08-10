import math

def mass_ratio(delta_v, exhaust_velocity):
    return math.exp(delta_v / exhaust_velocity)

def required_launch_mass(dry_mass, delta_v, exhaust_velocity):
    ratio = mass_ratio(delta_v, exhaust_velocity)
    return dry_mass * ratio

# Your rocket
dry_mass = 500
delta_v = 9400
exhaust_velocity = 3000

ratio = mass_ratio(delta_v, exhaust_velocity)
launch_mass = required_launch_mass(dry_mass, delta_v, exhaust_velocity)

print(f"Mass ratio needed: {ratio:.2f}")
print(f"Launch mass needed: {launch_mass:.2f} kg")
print(f"Fuel mass: {launch_mass - dry_mass:.2f} kg")
