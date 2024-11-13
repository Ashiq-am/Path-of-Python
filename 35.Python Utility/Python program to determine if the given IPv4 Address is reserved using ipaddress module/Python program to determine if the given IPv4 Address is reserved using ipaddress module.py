# importing ip_address
# from ipaddress module
from ipaddress import ip_address


def reservedIPAddress(IP: str) -> str:
    return "Reserved" if (ip_address(IP).is_reserved) else "Not Reserved"


if __name__ == '__main__':
    # Not Reserved
    print(reservedIPAddress('10.0.0.1'))

    # Reserved
    print(reservedIPAddress('241.0.0.133'))
