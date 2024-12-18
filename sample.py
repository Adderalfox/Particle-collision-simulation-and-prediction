import numpy as np

def generate_energy(min_energy=10, max_energy=100):
    return np.random.uniform(min_energy, max_energy)

def generate_collision_angle(min_angle=0, max_angle=180):
    return np.random.uniform(min_angle, max_angle)

def generate_momentum_vector():
    momentum_vector = np.random.uniform(-100, 100, size=3)
    return momentum_vector

def adjust_momentum_vector(energy, mass=0):
    c = 1
    # E^2 = (mc)^2 + (|p|c)^2
    momentum_magnitude = np.sqrt(energy**2 - (mass * c**2)**2) / c
    direction = generate_momentum_vector()
    unit_vector = direction / np.linalg.norm(direction)
    return unit_vector * momentum_magnitude

energy = generate_energy()

print(f"Generated Energy: {energy:.2f} GeV")
print(f"Generated Collision angle: {generate_collision_angle():.2f} degrees")
print(f"Generated momentum vector: {adjust_momentum_vector(energy):}")


