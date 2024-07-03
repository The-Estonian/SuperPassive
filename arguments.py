import argparse

def cl_arguments():
    parser = argparse.ArgumentParser(description="Welcome to passive v1.0.0")
    parser.add_argument("-fn", dest="Full_Name", help="Search with full-name")
    parser.add_argument("-ip", dest="IP_Address", help="Search with ip address")
    parser.add_argument("-u", dest="Username", help="Search with username")
    arguments = parser.parse_args()
    if not arguments.IP_Address or arguments.Username or arguments.Full_Name:
        print("Please specify an IP address, a username, or a full name. Use --help to see usage.\n")
    return arguments
