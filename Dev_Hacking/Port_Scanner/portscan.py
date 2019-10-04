# This Python file uses the following encoding: utf-8
import socket
import sys

def full_ports():
    print("Ports: 1 - 65535")
    print("\nPort  |  STATUS")
    for porta in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        code = sock.connect_ex((ip, porta))
        if (code == 0):
            print("{}     OPEN".format(porta))
            sock.close()
    print("\nThe port scan has been completed!")
    sys.exit()

def set_ports():
    port1 = int(input("Begin: "))
    port2 = int(input("end: "))
    print("-" * 30)
    print("\nPort |  STATUS")
    for porta in range(port1, port2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        code = sock.connect_ex((ip, porta))
        if (code == 0):
            print("{}     OPEN".format(porta))
            sock.close()
    print("\nThe port scan has been completed!")
    sys.exit()

def stage_ports():
        print("STAGE 1/3: 1 - 1024")
        print("-" * 60)
        print("\nPort  |  STATUS")
        for porta in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.05)
            code = sock.connect_ex((ip, porta))
            if code == 0:
                print("{}     OPEN".format(porta))
                sock.close()
            if porta == 1024:
                i = str(input("\nDo you want to continue port scanning? (Y/N) "))
                while i.upper() != "Y" and i.upper() != "N":
                    i = str(input("\nInvalid option, please re-enter your choice!" +
                                  "\nDo you want to continue port scanning? (Y/N) "))
                if i.upper() == "N":
                    print("\nThe port scan has been completed!!")
                    sys.exit()
                else:
                    print("-" * 60)
                    print("STAGE 2/3: 1025 - 20567")
                    print("-" * 60)
                    print("\nPort  |  STATUS")

            if porta == 20567:
                i = str(input("\nDo you want to continue port scanning? (Y/N) "))
                while i.upper() != "Y" and i.upper() != "N":
                    i = str(input("\nInvalid option, please re-enter your choice!" +
                                  "\nDo you want to continue port scanning? (Y/N) "))
                if i.upper() == "N":
                    print("\nThe port scan has been completed!!")
                    sys.exit()
                else:
                    print("-" * 60)
                    print("STAGE 3/3: 20567 - 65535")
                    print("-" * 60)
                    print("\nPort  |  STATUS")
        print("\nThe port scan has been completed!!")
        sys.exit()
try:
    print("-" * 60)
    scan = input("Enter Website/IP Address to be scanned: ")
    ip = socket.gethostbyname(scan)
    print("Wait... scanned ports on host: ", ip)
    print("-" * 60)
    i = str(input("Port Scanning - Menu" +
                  "\n\n1 - To scan all possible ports " +
                  "\n2 - To set a port range "
                  "\n3 - To scan step by step "
                  "\n\nEnter your option:  "))
    print("-" * 60)
    if i == "1":
        full_ports()
    elif i == "2":
        set_ports()
    elif i == "3":
        stage_ports()
    else: print("invalid option. Exiting...")

except socket.gaierror:
    print('\n\nHostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print("\n\nCouldn't connect to server")
    sys.exit()
except KeyboardInterrupt:
    print("\n\nYou pressed Control+C to stop the program")
    sys.exit()
