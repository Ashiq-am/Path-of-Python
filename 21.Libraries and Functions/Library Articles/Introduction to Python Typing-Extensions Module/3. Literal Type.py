from typing_extensions import Literal

def set_environment(env: Literal['development', 'production']) -> None:
    if env not in ['development', 'production']:
      raise Exception("Unknown env value!")
    print(f"Setting environment to {env}")

set_environment('development')
set_environment('staging') # Raises an error
