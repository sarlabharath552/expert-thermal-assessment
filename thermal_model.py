import math

# GIVEN DATA
Q = 150
Ta = 25
R_jc = 0.1

A_die = 0.002363

k_tim = 4
t_tim = 0.0001

k_al = 167
t_base = 0.0025

sink_length = 0.09
sink_width = 0.116
fin_height = 0.0245
fin_thickness = 0.0008
N_fins = 60

Sf = 0.001153

k_air = 0.0262
nu = 1.57e-5
Pr = 0.71
V = 1

# TIM resistance
R_tim = t_tim / (k_tim * A_die)

# Conduction resistance
R_cond = t_base / (k_al * A_die)

# Reynolds number
Re = (V * Sf) / nu

# Nusselt number
Nu = 1.86 * ((Re * Pr * (2 * Sf / sink_length)) ** (1/3))

# Heat transfer coefficient
h = (Nu * k_air) / (2 * Sf)

# Fin area
A_fin = 2 * sink_length * fin_height
A_fins_total = N_fins * A_fin

# Base exposed area
A_base_exposed = (sink_width * sink_length) - (N_fins * fin_thickness * sink_length)

A_total = A_fins_total + A_base_exposed

# Apply fin efficiency factor
fin_efficiency = 0.45
A_effective = A_total * fin_efficiency

# Convection resistance
R_conv = 1 / (h * A_effective)

# Heat sink resistance
R_hs = R_cond + R_conv

# Total resistance
R_total = R_jc + R_tim + R_hs

# Junction temperature
Tj = Ta + Q * R_total

print("Heat Sink Resistance:", round(R_hs,3))
print("Total Thermal Resistance:", round(R_total,3))
print("Junction Temperature:", round(Tj,2),"°C")