# Advanced fixture example
import nose.tools as nt

def setup():
    # Setup logic for advanced fixture
    print("Setting up advanced fixture")

def teardown():
    # Teardown logic for advanced fixture
    print("Tearing down advanced fixture")

@nt.with_setup(setup, teardown)
def test_advanced_fixture():
    # Test utilizing advanced fixture
    print("Testing with advanced fixture")
