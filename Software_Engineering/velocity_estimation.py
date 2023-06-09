""" Copyright (c) 2023 with MIT License,
    Author : Muhammet USLU

    Levenberg-Marquard based program computes the estimated absolute velocity (m/s) of a target
    with given radar range, azimuth angle and radial velocity of the corresponding point in radar measurement point cloud. """

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

log_dict = {"Iteration" : [], "Vx, Vy" : []}
def cost_function(params, vr, xi):
    """Helper function that calculates the difference between given radial velocity and formulated radial velocity.

    Args:
        params (float, float) : motion (optimization) parameters in meter/second of the target in x and y coordinates
        vr (array of floats) : doppler(radial) velocity of the target
        xi (array of floats) : azimuth angle in radian
    Returns:
        residuals (array of floats) : calculated differences for radial velocity
    """
    cost_function.counter += 1 # counts times of call of the cost function.
    vx, vy = params
    residuals = vr - vx * np.cos(xi) - vy * np.sin(xi)
    log_dict["Iteration"].append(cost_function.counter)
    log_dict["Vx, Vy"].append((round(vx, 3), round(vy, 3)))
    return residuals

cost_function.counter = 0

def target_velocity_estimation(range: np.ndarray, azimuth: np.ndarray, doppler: np.ndarray, initial):
    """Estimation algorithm based of Levenberg-Marquard that optimizes X and Y coordinate components of the absolute velocity of target subject to given dataset.

    Args:
        doppler (array of floats) : radial velocity(m/s) of the target according to radar beam
        azimuth (array of floats) : azimuth (rad), the deviating angle connects north of sensor beam and target
        initial_guess (float, float) : velocity values (m/s) in order to initiate optimization algorithm
    Returns:
        Vx, Vy (float, float) : Estimated X and Y coordinate components(m/s) of the absolute velocity of target
    """
    result = least_squares(cost_function, initial, args=(doppler, azimuth), verbose = 2, method = 'lm')
    Vx, Vy = result.x

    """ToDo : in order to optimize the algorithm consider
                    * pose(alpha) of the target.
                    * radial velocity and azimuth angle possibly have measurement errors -> Use fusion of two radar sensors,
                    it will result in an extended total azimuth area of the velocity profile."""

    return round(Vx, 3), round(Vy, 3)

### Example Usage ###
distance = np.array([10, 7, 5, 3.5, 2.7, 1.4])
Vr = np.array([100, 70, 50, 35, 27, 14])
phi_i = np.array([64, 51, 45, 39, 33, 30 ])
initial_guess = np.array([1.0, 1.0])

Vx_est, Vy_est = target_velocity_estimation(range = distance, azimuth = phi_i, doppler = Vr, initial = initial_guess)
df = pd.DataFrame(log_dict)
pd.set_option('colheader_justify', 'center')
print(df.to_string(index=False))

print(f"Estimated Vx: {Vx_est} m/s")
print(f"Estimated Vy: {Vy_est} m/s")
print(f"Estimated Absolute Velocity (V): {round(np.sqrt(Vx_est**2 + Vy_est**2), 3)} m/s")
