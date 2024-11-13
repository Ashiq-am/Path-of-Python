from ipaddress import ip_address, IPv4Address


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


if __name__ == '__main__':
    # Enter the Ip address
    Ip = "192.168.0.1"
    print(validIPAddress(Ip))

    Ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(validIPAddress(Ip))

    Ip = "256.32.555.5"
    print(validIPAddress(Ip))

    Ip = "250.32:555.5"
    print(validIPAddress(Ip))
