def generate_random_data(size, num_frames):
    data_frames = []
    for _ in range(num_frames):
        data = np.random.rand(size, size)
        df = pd.DataFrame(data)
        data_frames.append(df)
    return data_frames

size = 10  # Size of the correlation matrix
num_frames = 50  # Number of frames in the animation
data_frames = generate_random_data(size, num_frames)
