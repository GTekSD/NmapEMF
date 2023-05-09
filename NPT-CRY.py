#Tool for Network PT by GTekSD

import os

def run_nmap_script(script_cmd):
    os.system(script_cmd)

def display_menu():
    print("[i] Select a vulnerability to scan:")
    print(" 1. Microsoft SQL Server Unsupported Version Detection")
    print(" 2. Redis Server Unprotected by Password Authentication")
    print(" 3. SSL Version 2 and 3 Protocol Detection")
    print(" 4. TLS Version 1.0 Protocol Deprecated")
    print(" 5. TLS Version 1.1 Protocol Deprecated")
    print(" 6. SSL Certificate Signed Using Weak Hashing Algorithm")
    print(" 7. SSL Medium Strength Cipher Suites Supported (SWEET32)")
    print(" 8. SSL Certificate Chain Contains RSA Keys Less Than 2048 bits")
    print(" 9. OpenSSL AES-NI Padding Oracle MitM Information Disclosure")    
    print("10. SMB Signing not required")
    print("11. SSL Certificate Expiry")
    print("12. SSL / TLS Versions Supported")
    print("13. SSL RC4 Cipher Suites Supported (Bar Mitzvah)")
    print("14. SSL Self-Signed Certificate")
    print("15. SSL Cipher Suites Supported")
    print("16. SSL Weak Cipher Suites Supported")
    print("17. SSLv3 Padding Oracle on Downgraded Legacy Encryption Vulnerability (POODLE)")
    print("18. SSL/TLS Diffie-Hellman Modulus <= 1024 Bits (Logjam)")
    print("19. SSH Weak Key Exchange Algorithms Enabled")
    print("20. SSH Weak MAC Algorithms Enabled")
    print("21. HSTS Missing from HTTPS Server")
    print("22. SSH Protocol Version 1 Session Key Retrieval")
    print("23. IP Forwarding Enabled")
    print("24. SSH Server CBC Mode Ciphers Enabled")
    print("25. DHCP Server Detection")
    print("26. Unencrypted Telnet Server")

    choice = int(input("\n[i] Enter vulnerability number: "))
    
    if choice == 1:
        script_cmd = "nmap -p 445 --script ms-sql-info"
    elif choice == 2:
        script_cmd = "nmap -p 6379 --script redis-brute"
    elif choice == 3:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p 443"
    elif choice == 4:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p 443 --script-args ssl-enum-ciphers.min-protocol-version=TLSv1"
    elif choice == 5:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p 443 --script-args ssl-enum-ciphers.min-protocol-version=TLSv1.1"
    elif choice == 6:
        script_cmd = "nmap --script ssl-cert"
    elif choice == 7:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p 443 --script-args ssl-enum-ciphers.SWEET32=1"
    elif choice == 8:
        script_cmd = "nmap -p 64278 --script ssl-cert"
    elif choice == 9:
        script_cmd = "nmap --script ssl-ccs-injection"   
    elif choice == 10:
        script_cmd = "nmap --script smb2-security-mode.nse -p 445"
    elif choice == 11:
        script_cmd = "nmap --script ssl-cert"                
    elif choice == 12:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p 443"
    elif choice == 13:
        script_cmd = "nmap --script ssl-enum-ciphers -p 443"
    elif choice == 14:
        script_cmd = "nmap --script ssl-cert"
    elif choice == 15:
        script_cmd = "nmap -sV --script ssl-enum-ciphers -p <PORT>"
    elif choice == 16:
        script_cmd = "nnmap -sV --script ssl-enum-ciphers -p <PORT>"
    elif choice == 17:
        script_cmd = "nmap -sV --version-light --script ssl-poodle -p 443"
    elif choice == 18:
        script_cmd = "nmap --script ssl-dh-params"
    elif choice == 19:
        script_cmd = "nmap --script ssh2-enum-algos"
    elif choice == 20:
        script_cmd = "nmap -Pn -p22 --script ssh2-enum-algos"
    elif choice == 21:
        script_cmd = "nmap -p <PORT> --script http-security-headers"
    elif choice == 22:
        script_cmd = "nmap -sV -sC"
    elif choice == 23:
        script_cmd = "nmap -sn --script ip-forwarding"
    elif choice == 24:
        script_cmd = "nmap --script ssh2-enum-algos"
    elif choice == 25:
        script_cmd = "nmap -sU -p 67 --script=dhcp-discover"
    elif choice == 26:
        script_cmd = "nmap -p 23 -script telnet-encryption"     
    else:
        print("Invalid choice.")
        return

    host = input("[|] Enter IP address to scan: ")
    script_cmd = f"{script_cmd} {host}"

    print("\n[i] CMD ======================================================================================================" )
    print(script_cmd)
    print("\n[i]  =========================================================================================================" )

    run_nmap_script(script_cmd)

display_menu()
