#!/usr/bin/env python3
"""
Vaccine Effectiveness Calculator

This script provides a simple function to calculate vaccine effectiveness
based on cases in vaccinated and unvaccinated groups.
"""

def calculate_ve(cases_unvaccinated: int, cases_vaccinated: int) -> float:
    """
    Calculate vaccine effectiveness (VE) percentage.

    Parameters:
    -----------
    cases_unvaccinated : int
        Number of influenza cases in the unvaccinated group.
    cases_vaccinated : int
        Number of influenza cases in the vaccinated group.

    Returns:
    --------
    float
        Vaccine effectiveness as a percentage (0-100).

    Formula:
    --------
    VE = (1 - (cases_vaccinated / cases_unvaccinated)) * 100

    Assumptions:
    ------------
    This simplified formula assumes equal population sizes in both groups
    and that all other factors are equal. For real-world analysis, more
    sophisticated methods should be used.
    """
    if cases_unvaccinated == 0:
        raise ValueError("cases_unvaccinated cannot be zero.")
    risk_ratio = cases_vaccinated / cases_unvaccinated
    ve = (1 - risk_ratio) * 100
    return ve


if __name__ == "__main__":
    # Example usage
    unvac = 100
    vac = 20
    try:
        result = calculate_ve(unvac, vac)
        print(f"Vaccine Effectiveness: {result:.1f}%")
    except ValueError as e:
        print(f"Error: {e}")