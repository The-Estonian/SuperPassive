from checkIp import checkIp
from arguments import cl_arguments
from writeToFile import save_to_file
from socialMedia import find_username
from fullName import fullName

def main():
    args = cl_arguments()
    if args.IP_Address:
        save_to_file(checkIp(args.IP_Address), "result.txt")
    elif args.Username:
        find_username(args.Username)
    elif args.Full_Name:
        fullName(args.Full_Name)

if __name__ == "__main__":
    main()
    
