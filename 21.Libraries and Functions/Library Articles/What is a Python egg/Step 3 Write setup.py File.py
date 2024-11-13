# setup.py
from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'example_script = example_package.example_module:greet'
        ]
    },
    author='Your Name',
    author_email='your@email.com',
    description='A simple example package',
    url='https://github.com/your_username/example_package',
)
