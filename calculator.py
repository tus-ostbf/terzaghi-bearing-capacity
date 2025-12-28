"""
Terzaghi Bearing Capacity Calculator

This module implements the classic Terzaghi bearing capacity equation for shallow strip footings.
"""

import math


def calculate_terzaghi(c, phi, gamma, B, Df, q=None):
    """
    Calculate the ultimate bearing capacity of a shallow strip footing using Terzaghi's equation.

    Parameters
    ----------
    c : float
        Cohesion of soil (kPa).
    phi : float
        Friction angle of soil (degrees).
    gamma : float
        Unit weight of soil (kN/m³).
    B : float
        Width of footing (m).
    Df : float
        Depth of foundation (m).
    q : float, optional
        Effective overburden pressure at foundation base (kPa). If not provided,
        calculated as gamma * Df.

    Returns
    -------
    q_ult : float
        Ultimate bearing capacity (kPa).
    """
    # Convert phi from degrees to radians for trigonometric functions
    phi_rad = math.radians(phi)

    # Calculate bearing capacity factors (Terzaghi's formulas)
    # N_q = e^(π tan φ) * tan²(π/4 + φ/2)
    n_q = math.exp(math.pi * math.tan(phi_rad)) * (math.tan(math.pi/4 + phi_rad/2) ** 2)

    # N_c = (N_q - 1) * cot φ (for φ > 0)
    if phi == 0:
        # For purely cohesive soil (φ=0), N_c = 5.7 (per Terzaghi)
        n_c = 5.7
    else:
        n_c = (n_q - 1) * (1.0 / math.tan(phi_rad))

    # N_γ = (N_q - 1) * tan(1.4 φ) (approximate)
    n_gamma = (n_q - 1) * math.tan(1.4 * phi_rad)

    # Overburden pressure
    if q is None:
        q = gamma * Df

    # Terzaghi equation for strip footing
    q_ult = c * n_c + q * n_q + 0.5 * gamma * B * n_gamma

    return q_ult


if __name__ == "__main__":
    # Example usage
    c = 25.0  # kPa
    phi = 20.0  # degrees
    gamma = 18.0  # kN/m³
    B = 2.0  # m
    Df = 1.5  # m

    q_ult = calculate_terzaghi(c, phi, gamma, B, Df)
    print(f"Cohesion: {c} kPa")
    print(f"Friction angle: {phi}°")
    print(f"Unit weight: {gamma} kN/m³")
    print(f"Footing width: {B} m")
    print(f"Foundation depth: {Df} m")
    print(f"Ultimate bearing capacity: {q_ult:.2f} kPa")