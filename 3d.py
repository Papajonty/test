import numpy as np

def pipe_network_analysis(diameters, velocities, pressure_drops, roughnesses, fluid_density, fluid_viscosity):
    """
    Analyze fluid flow in a pipe network
    
    Parameters:
    diameters (list): List of pipe diameters (m)
    velocities (list): List of fluid velocities (m/s)
    pressure_drops (list): List of pressure drops (Pa)
    roughnesses (list): List of pipe roughnesses (m)
    fluid_density (float): Density of fluid in kg/m^3
    fluid_viscosity (float): Dynamic viscosity of fluid in Pa.s
    
    Returns:
    energy_losses (list): List of energy losses (J) due to friction
    """
    energy_losses = []
    for i in range(len(diameters)):
        diameter = diameters[i]
        velocity = velocities[i]
        pressure_drop = pressure_drops[i]
        roughness = roughnesses[i]
        
        # Calculate the Reynolds number
        Re = fluid_density * velocity * diameter / fluid_viscosity
        
        # Calculate the Darcy friction factor using the Colebrook equation
        f = 0.25 / (np.log10(roughness / (3.7 * diameter) + 5.74 / (Re * 0.9))) * 2
        
        # Calculate the energy loss due to friction
        energy_loss = pressure_drop * (velocity ** 2) / (2 * f * fluid_density)
        energy_losses.append(energy_loss)
    
    return energy_losses

# Example usage
diameters = [0.05, 0.06, 0.07]
velocities = [1, 2, 3]
pressure_drops = [100, 200, 300]
roughnesses = [0.001, 0.002, 0.003]
fluid_density = 1000 # kg/m^3
fluid_viscosity = 0.001 # Pa.s
energy_losses = pipe_network_analysis(diameters, velocities, pressure_drops, roughnesses, fluid_density, fluid_viscosity)
print(energy_losses)
