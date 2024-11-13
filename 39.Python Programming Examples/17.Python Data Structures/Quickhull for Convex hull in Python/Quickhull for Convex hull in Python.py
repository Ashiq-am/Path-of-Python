def find_distance(p1, p2, p):
    """
    Calculate the distance between a point p and the line formed by p1 and p2.
    """
    return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

def quickhull(points):
    """
    Find the convex hull of a set of points using the Quickhull algorithm.

    Parameters:
        points (list): A list of (x, y) coordinate tuples representing the points.

    Returns:
        list: A list of (x, y) coordinate tuples representing the convex hull.
    """
    if len(points) <= 1:
        return points

    def hull(p1, p2, points):
        """
        Find the points in the input set that lie outside the triangle formed by p1, p2, and the convex hull.
        """
        if not points:
            return []

        farthest_point = max(points, key=lambda p: abs(find_distance(p1, p2, p)))
        next_points = [p for p in points if find_distance(p1, farthest_point, p) > 0]
        return hull(p1, farthest_point, next_points) + [farthest_point] + hull(farthest_point, p2, next_points)

    min_point = min(points)
    max_point = max(points)
    convex_hull = hull(min_point, max_point, points) + hull(max_point, min_point, points)
    return sorted(set(convex_hull))

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = quickhull(points)
print("Convex Hull Points:", convex_hull)
