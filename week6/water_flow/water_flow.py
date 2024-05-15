# Created by Alex Dombroski 1/24/24
# Computation function headings, global variables, and main function taken from CSE 111 course material and edited


# ---------- Computation Functions ----------

def water_column_height(p_tower_height, p_tank_height):
    # calculates and returns the height of a column of water from a tower height and a tank wall height.
    return p_tower_height + 3 * p_tank_height / 4

def pressure_gain_from_water_height(p_height):
    # calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.
    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * p_height / 1000

def pressure_loss_from_pipe(p_pipe_diameter, p_pipe_length, p_friction_factor, p_fluid_velocity):
    # calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.
    return -p_friction_factor * p_pipe_length * WATER_DENSITY * p_fluid_velocity * p_fluid_velocity / 2000 / p_pipe_diameter

def pressure_loss_from_fittings(p_fluid_velocity, p_quantity_fittings):
    # calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline.
    return -0.04 * WATER_DENSITY * p_fluid_velocity * p_fluid_velocity * p_quantity_fittings / 2000

def reynolds_number(p_hydraulic_diameter, p_fluid_velocity):
    # calculates and returns the Reynolds number for a pipe with water flowing through it. The Reynolds number is 
    # a unitless ratio of the inertial and viscous forces in a fluid that is useful for predicting fluid flow in different situations.
    return WATER_DENSITY * p_hydraulic_diameter * p_fluid_velocity / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(p_larger_diameter, p_fluid_velocity, p_reynolds_number, p_smaller_diameter):
    # calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter.
    k = (0.1 + 50 / p_reynolds_number) * ((p_larger_diameter / p_smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * p_fluid_velocity * p_fluid_velocity / 2000

def ad_kilopascals_to_psi(p_kilopascals):
    return p_kilopascals / 6.895

# ---------- Input/Output Functions ----------

def ad_get_valid_number(p_input_prompt):
    ad_invalid_input = True
    while ad_invalid_input:
        ad_input_value = input(p_input_prompt)
        try:
            float(ad_input_value)
        except:
            print("Please input a valid number")
        else:
            ad_invalid_input = False
    return float(ad_input_value)

def ad_display_pressure(p_pressure):
    print(f"Pressure at house: {p_pressure:.1f} kilopascals or {ad_kilopascals_to_psi(p_pressure):.1f} psi")

# ---------- Global Variables ----------

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016
EARTH_ACCELERATION_OF_GRAVITY = 9.80665

# ---------- Main ----------

def main():
    tower_height = ad_get_valid_number("Height of water tower (meters): ")
    tank_height = ad_get_valid_number("Height of water tank walls (meters): ")
    length1 = ad_get_valid_number("Length of supply pipe from tank to lot (meters): ")
    quantity_angles = ad_get_valid_number("Number of 90° angles in supply pipe: ")
    length2 = ad_get_valid_number("Length of pipe from supply to house (meters): ")

    water_height = water_column_height(tower_height, tank_height)
    
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    ad_display_pressure(pressure)

if __name__ == "__main__":
    main()