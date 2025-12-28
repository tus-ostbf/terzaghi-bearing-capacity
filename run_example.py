"""
Example script for Terzaghi bearing capacity calculator.
"""

from calculator import calculate_terzaghi


def main():
    # Sample case from the problem statement
    c = 25.0  # kPa
    phi = 20.0  # degrees
    gamma = 18.0  # kN/m³
    B = 2.0  # m
    Df = 1.5  # m

    q_ult = calculate_terzaghi(c, phi, gamma, B, Df)
    print("Terzaghi Bearing Capacity Calculation")
    print("=====================================")
    print(f"Cohesion (c): {c} kPa")
    print(f"Friction angle (φ): {phi}°")
    print(f"Unit weight (γ): {gamma} kN/m³")
    print(f"Footing width (B): {B} m")
    print(f"Foundation depth (Df): {Df} m")
    print(f"\nUltimate bearing capacity (q_ult): {q_ult:.2f} kPa")


if __name__ == "__main__":
    main()