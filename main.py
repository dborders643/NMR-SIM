from vpython import canvas, vector, arrow, color, sphere
import random

# 3D Canvas
scene = canvas(title="Vector Field in VPython",
               width=1200, height=600,
               center=vector(0, 0, 0),
               background=color.black)

# Parameters
h_rad = 1    # atom radius (abritrary unit)
B_mag = 1       # in Telsa (T)

# Parameters for grid
grid_range = range(-20, 21, 2)

# Static B field from Neodynium Magnets
def B_field(x, y, z):
    return vector(B_mag, 0, 0)

# Initialize B field plane
for x in grid_range:
    for y in grid_range:
        field_vec = B_field(x, y, 0)
        arrow(pos=vector(x, y, 0),
                axis=field_vec,
                color=color.blue,
                shaftwidth=0.1)

# Initialize Hydrogen Atoms
atoms = []
n_atoms = 20
spread = 15

for i in range(n_atoms):
    x = random.uniform(-spread, spread)
    y = random.uniform(-spread, spread)
    z = random.uniform(-spread, spread)
    atom = sphere(pos=vector(x, y, z), radius=h_rad, color=color.white)
    atoms.append(atom)


# Keep the scene open
scene.waitfor('click')
