import math

def angle_between_vectors(u, v):
    dot_product = sum(i*j for i, j in zip(u, v))
    norm_u = math.sqrt(sum(i**2 for i in u))
    norm_v = math.sqrt(sum(i**2 for i in v))
    cos_theta = dot_product / (norm_u * norm_v)
    angle_rad = math.acos(cos_theta)
    angle_deg = math.degrees(angle_rad)
    return angle_rad, angle_deg
# Example usage
vector_u = [3, 4]  # Vector u = (3, 4)
vector_v = [5, -2]  # Vector v = (5, -2)
angle_rad, angle_deg = angle_between_vectors(vector_u, vector_v)
print(f"Angle between vectors (in radians): {angle_rad}")
print(f"Angle between vectors (in degrees): {angle_deg}")
