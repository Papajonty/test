import math


def pressure_drop(v1, v2, h1, h2, rho):
    """
    Calculate pressure drop using Bernoulli's equation and the continuity equation.

    Parameters:
    v1 (float): initial fluid velocity (m/s)
    v2 (float): final fluid velocity (m/s)
    h1 (float): initial fluid height (m)
    h2 (float): final fluid height (m)
    rho (float): fluid density (kg/m^3)

    Returns:
    float: pressure drop (Pa)
    """
    g = 9.81  # acceleration due to gravity (m/s^2)
    p1 = rho * g * h1  # pressure at initial height (Pa)
    p2 = rho * g * h2  # pressure at final height (Pa)
    delta_p = 0.5 * rho * (v1*2 - v2*2) + (p1 - p2)  # pressure drop (Pa)
    return delta_p


# Example usage
delta_p = pressure_drop(v1=1, v2=2, h1=2, h2=1, rho=1000)
print("Pressure drop: {:.2f} Pa".format(delta_p))
