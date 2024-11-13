def monte_carlo_pi(num_samples):

    # 1. Initialize counters for points inside and outside the circle.
    inside_circle = 0

    # 2. Perform the specified number of random trials.
    for _ in range(num_samples):
        # 3. Generate random coordinates (x, y) within the unit square.
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # 4. Check if the point is inside the unit circle (x^2 + y^2 <= 1).
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # 5. Estimate pi using the ratio of points inside the circle
    # to the total number of trials.
    return 4 * inside_circle / num_samples
