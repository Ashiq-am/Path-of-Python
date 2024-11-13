import os
import pypandoc

# Ensure pypandoc is installed
try:
    import pypandoc
except ImportError:
    print("pypandoc is not installed. Installing now...")
    os.system('pip install pypandoc')

# Ensure pandoc is installed
pandoc_installed = os.system('pandoc --version') == 0
if not pandoc_installed:
    print("pandoc is not installed. Installing now...")
    os.system('sudo apt-get install pandoc')  # or brew install pandoc for macOS

# Verify installation
try:
    output = pypandoc.convert_text('# Hello World', 'rst', format='md')
    print("pypandoc is working correctly!")
    print(output)
except OSError as e:
    print(f"Error using pypandoc: {e}")
