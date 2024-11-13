import os

for cert in ['sslrootcert', 'sslcert', 'sslkey']:
    if cert in conn_params and not os.path.isfile(conn_params[cert]):
        raise FileNotFoundError(f"Certificate file {conn_params[cert]} not found.")
