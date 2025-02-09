import glob
files = glob.glob("data/*.csv")
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
