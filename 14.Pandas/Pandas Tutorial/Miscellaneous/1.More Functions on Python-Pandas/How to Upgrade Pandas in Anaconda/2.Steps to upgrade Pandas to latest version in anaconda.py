import subprocess

# Running the command to update conda
update_conda = subprocess.run(['conda', 'update', 'conda', '-y'], capture_output=True, text=True)
print("Updating Conda:")
print(update_conda.stdout)

# Running the command to install pandas 2.0
install_pandas = subprocess.run(['conda', 'install', 'pandas=2.0', '-y'], capture_output=True, text=True)
print("Installing Pandas 2.0:")
print(install_pandas.stdout)
