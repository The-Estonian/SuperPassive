from checkIp import checkIp
from arguments import cl_arguments
from writeToFile import save_to_file

def main():
    args = cl_arguments()
    if args.IP_Address:
        save_to_file(checkIp(args.IP_Address), "result.txt")
    elif args.Username:
        print(f"Tracking username: {args.Username}")
    elif args.Full_Name:
        print(f"Tracking full name: {args.Full_Name}")

if __name__ == "__main__":
    main()
    
