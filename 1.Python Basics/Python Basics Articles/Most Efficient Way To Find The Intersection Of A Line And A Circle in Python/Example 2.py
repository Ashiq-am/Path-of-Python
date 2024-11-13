import math


def find_intersections(h, k, r, m, c):
    A = 1 + m**2
    B = 2 * (m * (c - k) - h)
    C = h**2 + (c - k)**2 - r**2

    discriminant = B**2 - 4 * A * C

    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -B / (2 * A)
        y = m * x + c
        return [(x, y)]
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-B + sqrt_discriminant) / (2 * A)
        x2 = (-B - sqrt_discriminant) / (2 * A)
        y1 = m * x1 + c
        y2 = m * x2 + c
        return [(x1, y1), (x2, y2)]


# Example usage
h, k, r = 0, 0, 12  # Circle with center (0,0) and radius 12
m, c = 0, 5        # Line y = x

intersections = find_intersections(h, k, r, m, c)
print(intersections)
