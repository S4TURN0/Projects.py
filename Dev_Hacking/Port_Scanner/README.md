## Scan Network Ports

#### The port scanner tool will provide you with information regarding valid methods of connecting to a network. Scanning your network for open ports and determinning if those open ports need to be closed to provide more network security.

## What is a port?

#### Network ports are used for routing incoming information from a network to specific applications to a designated machine. Example, if you wanted to enable Remote Desktop on a Windows PC within your network, you'd need to make sure port 3389 was open and forwarding to the appropriate computer.
###### 


## O que é uma porta?
#### As portas de rede são usadas para rotear as informações recebidas de uma rede para aplicativos específicos para uma máquina designada. Por exemplo, se você deseja habilitar a Área de Trabalho Remota em um PC com Windows na sua rede, precisará garantir que a porta 3389 esteja aberta e encaminhada para o computador apropriado.

## Varredura de portas da rede
#### A ferramenta de verificação de portas fornecerá informações sobre métodos válidos de conexão com uma rede. Examinando a sua rede em busca de portas abertas, no qual você poderá determinar se essas portas precisam ser fechadas para fornecer mais segurança à rede.


### Service Name and Transport Protocol Port Number Registry
#### Basic

    21 - File Transfer Protocol (FTP)
    22 - Secure File Transfer Protocol (SFTP)
    25 - Simple Mail Transfer Protocol (SMTP)
    26 - [threat] W32.Netsky
    80 - Hypertext Transfer Protocol (HTTP)
    110 - Post Office Protocol v3 (POP3)
    143 - Internet Message Access Protocol (IMAP)
    443 - Hypertext Transfer Protocol over TLS/SSL (HTTPS)
    587 - Simple Mail Transfer Protocol (Often more secure than port 25)
    993 - Internet Message Access Protocol over TLS/SSL (IMAPS)
    995 - Post Office Protocol 3 over TLS/SSL (POP3S)
    2525 - Remote Access Trojans
    3306 - MySQL database system

#### Web - Scans ports in the Basic Package plus the ports below

    23 - Telnet protocol - unencrypted text communications
    43 - WHOIS protocol
    53 - Domain Name System (DNS)
    67 - Dynamic Host Configuration Protocol (DHCP) and Bootstrap Protocol (BOOTP) server
    68 - Dynamic Host Configuration Protocol (DHCP) and Bootstrap Protocol (BOOTP) client
    69 - Trivial File Transfer Protocol (TFTP)
    123 - Network Time Protocol (NTP) - time synchronization
    137 - NetBIOS Name Service
    138 - NetBIOS Datagram Service
    139 - NetBIOS Session Service
    161 - Simple Network Management Protocol (SNMP)
    162 - Simple Network Management Protocol Trap (SNMPTRAP)
    389 - Lightweight Directory Access Protocol (LDAP)
    636 - Lightweight Directory Access Protocol over TLS/SSL (LDAPS)
    989 - FTPS Protocol (data), FTP over TLS/SSL
    990 - FTPS Protocol (control), FTP over TLS/SSL
    2077 - TrelliSoft Agent
    2078 - TrelliSoft Server
    2082 - cPanel default
    2083 - Secure RADIUS Service (radsec)
    2086 - WebHost Manager default
    2087 - WebHost Manager default SSL
    2095 - cPanel web mail default
    2096 - cPanel SSL web mail default

#### Games

    1725 - Valve Steam Client
    2302 - ArmA and Halo: Combat Evolved
    3074 - Xbox Live and/or Games for Windows Live
    3724 - World of Warcraft
    6112 - Blizzard's Battle.net Gaming Service
    6500 - Gamespy Arcade, Unreal, Tony Hawk, Warhammer, Starwars, Civilization III and IV, BoKS Master, Command & Conquer
    12035 - Linden Lab viewer to sim on SecondLife
    12036 - Second Life
    14567 - Battlefield 1942
    25565 - Minecraft Dedicated Server
    27015 - GoldSrc and Source engine dedicated server port
    28960 - Call of Duty

#### Malicious

    1080 - W32.Beagle, WinHole, W32.HLLW.Deadhat, and several others like keyloggers, remote peekers, etc.
    2745 - Bagle Virus Backdoor
    3127 - W32.Mockbot, W32.Solame, and others
    4444 - Metasploit's default listener port
    5554 - W32.Dabber and W32.Sasser
    8866 - W32.Beagle
    9898 - CrashCool and W32.Dabber
    9988 - Used by many trojans and worms
    12345 - Used by many trojans and worms
    27374 - Used by many trojans, remote access hacks, worms, etc.
    31337 - Used by many trojans and worms
