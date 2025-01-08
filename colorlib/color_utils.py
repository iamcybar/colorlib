def hex_to_rgb(hex_color: str) -> tuple:
    """
    Convert a HEX color to an RGB tuple.

    Args:
        hex_color (str): A HEX color string (e.g., '#FFFFFF').

    Returns:
        tuple: An (R, G, B) tuple.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color: tuple) -> str:
    """
    Convert an RGB tuple to a HEX color.

    Args:
        rgb_color (tuple): An (R, G, B) tuple.

    Returns:
        str: A HEX color string (e.g., '#FFFFFF').
    """
    return '#{:02X}{:02X}{:02X}'.format(*rgb_color)


def complement_color(hex_color: str) -> str:
    """
    Get the complementary HEX color.

    Args:
        hex_color (str): A HEX color string (e.g., '#FFFFFF').

    Returns:
        str: The complementary HEX color.
    """
    rgb = hex_to_rgb(hex_color)
    comp_rgb = tuple(255 - c for c in rgb)
    return rgb_to_hex(comp_rgb)
