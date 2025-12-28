# Terzaghi Bearing Capacity Project

A collaborative, version-controlled educational tool that calculates the ultimate bearing capacity of a shallow strip footing using the classic Terzaghi equation.

## Background

Terzaghi's bearing capacity equation is a cornerstone of foundation engineering, detailed in foundational texts like NAVFAC DM 7.02. The equation is:

```
q_ult = c * N_c + q * N_q + 0.5 * γ * B * N_γ
```

Where:
- `q_ult` is the ultimate bearing capacity.
- `c` is the soil cohesion.
- `q` is the effective overburden pressure at the foundation base.
- `γ` is the unit weight of the soil.
- `B` is the footing width.
- `N_c`, `N_q`, and `N_γ` are the bearing capacity factors, which are functions of the soil's friction angle (φ).

## Repository Structure

The repository will contain:

- `calculator.py`: Python module implementing the Terzaghi bearing capacity calculation.
- `run_example.py`: Example script demonstrating usage.
- `README.md`: Project documentation.
- `tests/`: Unit tests for validation.
- `docs/`: Additional documentation and references.

## Development Plan

1. **Initial version**: Implement core calculation for strip footings.
2. **Enhancements**: Add shape factors for square, circular, rectangular footings.
3. **Validation**: Input validation and error handling.
4. **Documentation**: Detailed usage examples and API reference.
5. **Testing**: Comprehensive test suite with edge cases.

## Usage

To use the calculator, import the function `calculate_terzaghi` from `calculator.py`. Provide soil parameters and geometry.

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.