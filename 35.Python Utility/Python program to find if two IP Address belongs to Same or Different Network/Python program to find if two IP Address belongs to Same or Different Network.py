# importing ip_network from ipaddress module
from ipaddress import ip_network


def sameNetwork(IP1: str, IP2: str) -> str:
    a = ip_network(IP1, strict=False).network_address
    b = ip_network(IP2, strict=False).network_address

    if (a == b):
        return "Same Network"

    else:
        return "Different Network"


# main function
if __name__ == '__main__':
    # Same Network
    print(sameNetwork('192.168.1.0/8', '192.32.45.7/8'))

    # Different Network
    print(sameNetwork('17.53.128.0/20', '17.53.127.0/20'))

