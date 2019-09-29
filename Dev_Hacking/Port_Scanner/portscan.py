# This Python file uses the following encoding: utf-8
import socket
import sys

def FullPorts():
    print("Portas: 1 - 65535")
    print("\nPort  |  STATUS")
    for porta in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        code = sock.connect_ex((ip, porta))
        if (code == 0):
            print("{}     OPEN".format(porta))
            sock.close()
    print("\nEscaneamento Completo!")
    sys.exit()

def FaixaPorts():
    port1 = int(input("Inicio: "))
    port2 = int(input("Final: "))
    print("-" * 30)
    print("\nPort |  STATUS")
    for porta in range(port1, port2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        code = sock.connect_ex((ip, porta))
        if (code == 0):
            print("{}     OPEN".format(porta))
            sock.close()
    print("\nEscaneamento Completo!")
    sys.exit()

def EtapaPorts():
        print("ETAPA 1/3: 1 - 1024")
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
                i = str(input("\nDeseja continuar o PortScan? (Y/N) "))
                while i != "Y" and i != "N":
                    i = str(input("\nOpção invalida, por gentileza, digite novamente sua opção" +
                                  "\nDeseja continuar o PortScan? (Y/N) "))
                if i == "N":
                    print("\nEscaneamento Completo!")
                    sys.exit()
                else:
                    print("-" * 60)
                    print("ETAPA 2/4: 1025 - 20567")
                    print("-" * 60)
                    print("\nPort  |  STATUS")

            if porta == 20567:
                i = str(input("\nDeseja continuar o PortScan? (Y/N) "))
                while i != "Y" and i != "N":
                    i = str(input("\n Opção invalida, por gentileza, digite novamente sua opção" +
                                  "\nDeseja continuar o PortScan? (Y/N) "))
                if i == "N":
                    print("\nEscaneamento Completo!")
                    sys.exit()
                else:
                    print("-" * 60)
                    print("ETAPA 3/3: 20567 - 65535")
                    print("-" * 60)
                    print("\nPort  |  STATUS")
        print("\nEscaneamento Completo!")
        sys.exit()
try:
    print("-" * 60)
    scan = input("Enter Website/IP Address to be scanned: ")
    ip = socket.gethostbyname(scan)
    print("Wait... scanned ports on host: ", ip)
    print("-" * 60)
    i = str(input("OPCOES DO PORTSCAN" +
                  "\n1 - Para scanear todas as portas possiveis " +
                  "\n2 - Para definir uma faixa de portas"
                  "\n3 - Para scanear por etapas "
                  "\nDigite sua opçao: "))
    print("-" * 60)
    if i == "1":
        FullPorts()
    elif i == "2":
        FaixaPorts()
    elif i == "3":
        EtapaPorts()
    else: print("Opção invalida")

except socket.gaierror:
    print('\n\nHostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print("\n\nCouldn't connect to server")
    sys.exit()
except KeyboardInterrupt:
    print("\n\nYou pressed Control+C to stop the program")
    sys.exit()