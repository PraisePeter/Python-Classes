import socket

def identify_ip(ip):
    ip = ip.strip()

    # Check for IPv4
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return "IPv4"
    except socket.error:
        pass

    # Check for IPv6
    try:
        socket.inet_pton(socket.AF_INET6, ip)
        return "IPv6"
    except socket.error:
        pass

    return "Invalid"

def main():
    print("=== IP Address Identifier ===")
    print("Type 'quit' to exit\n")

    while True:
        ip = input("Enter an IP address: ").strip()

        if ip.lower() == 'quit':
            print("Goodbye!")
            break

        if not ip:
            print("Please enter an IP address.\n")
            continue

        result = identify_ip(ip)
        print(f"Result: '{ip}' --> {result}\n")


main()