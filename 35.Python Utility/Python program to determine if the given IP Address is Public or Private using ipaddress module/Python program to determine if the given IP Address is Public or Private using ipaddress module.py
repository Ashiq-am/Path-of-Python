# importing ip_address from
# ip address module
from ipaddress import ip_address


def IPAddress(IP: str) -> str:
    return "Private" if (ip_address(IP).is_private) else "Public"


if __name__ == '__main__':
    # Public IP
    print(IPAddress('17.5.7.8'))

    # Private IP
    print(IPAddress('172.16.0.10'))
