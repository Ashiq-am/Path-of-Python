try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])

except subprocess.CalledProcessError as e:
    # Output generated before error
    out_bytes = e.output
    # Return code
    code = e.returncode
