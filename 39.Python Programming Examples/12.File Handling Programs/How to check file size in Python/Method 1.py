from pathlib import Path

sz = Path('Data.csv').stat().st_size

print(sz)
