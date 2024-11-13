import numpy as np

def angle_between_vectors_np(u, v):
    u = np.array(u)
    v = np.array(v)
    cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    return angle_rad, angle_deg
# Example usage
vector_u = [3, 4]  # Vector u = (3, 4)
vector_v = [5, -2]  # Vector v = (5, -2)
angle_rad, angle_deg = angle_between_vectors_np(vector_u, vector_v)
print(f"Angle between vectors (in radians): {angle_rad}")
print(f"Angle between vectors (in degrees): {angle_deg}")
