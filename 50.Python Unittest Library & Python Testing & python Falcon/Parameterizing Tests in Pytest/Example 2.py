# Importing the Pytest library
import pytest

# Creating first test case
@pytest.mark.parametrize("input, output",
						[("Geeks For Geeks",
						"eeks For eeks"),
						("Go Air", "o Air"), ])
def test_remove_G(input, output):
	assert input.replace('G','')==output

# Creating second test case
@pytest.mark.parametrize("input, output",
						[("Geeks For Geeks",
							"Gaks For Gaks"),
							("Engineer", "Enginr"), ])
def test_e(input, output):
	assert input.replace('e','')==output
