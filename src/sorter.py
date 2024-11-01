def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Categorizes a package based on its dimensions and mass into the appropriate stack.

    """
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be positive numbers.")

    # Check if the package is bulky based on individual dimensions first
    is_bulky = width >= 150 or height >= 150 or length >= 150
    if not is_bulky:
        # Only calculate volume if none of the dimensions are over 150 cm
        is_bulky = (width * height * length) >= 1_000_000

    # Check if the package is heavy
    is_heavy = mass >= 20

    # Determine the category based on the criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
