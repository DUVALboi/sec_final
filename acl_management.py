import logging
from ssh_connection import SSHConnection

def configure_acl(router_name, router_ip, acl_commands):
    try:
        logging.info(f"Configuring ACL on {router_name} ({router_ip})...")
        ssh_conn = SSHConnection(router_ip, 'admin1', 'ssh/id_rsa')
        ssh_conn.establish_ssh_connection()
        ssh_conn.execute_commands(acl_commands)
        ssh_conn.close_connection()
        logging.info(f"ACL configuration applied to {router_name} ({router_ip}).")
    except Exception as e:
        logging.error(f"An error occurred while configuring {router_name}: {e}")

def configure_acl_gnb_router():
    acl_commands = [
        "configure terminal",
        "ip access-list extended ALLOW_SPECIFIC_IPS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " permit ip 192.168.99.0 0.0.0.255 192.169.98.0 0.0.0.255",
        " permit ip 192.169.98.0 0.0.0.255 192.168.99.0 0.0.0.255",
        " permit ip 192.168.10.0 0.0.0.255 any",
        " permit ip 192.168.20.0 0.0.0.255 any",
        " permit ip 192.168.30.0 0.0.0.255 any",
        " permit ip 192.169.10.0 0.0.0.255 any",
        " permit ip 192.169.20.0 0.0.0.255 any",
        " permit ip 192.169.30.0 0.0.0.255 any",
        " permit ip 11.11.11.0 0.0.0.3 any",
        " permit ip 12.12.12.0 0.0.0.3 any",
        " permit ip 200.0.150.0 0.0.0.3 any",
        " permit ip 200.100.150.0 0.0.0.3 any",
        " deny ip any any",
        "ip access-list extended MGMT_ACCESS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " deny ip any any",
        "interface GigabitEthernet0/1",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "interface GigabitEthernet0/6",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "interface GigabitEthernet0/7",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "end",
        "write memory"
    ]
    configure_acl("GnB_Router", "11.11.11.1", acl_commands)

def configure_acl_toisp_router():
    acl_commands = [
        "configure terminal",
        "ip access-list extended ALLOW_SPECIFIC_IPS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " permit ip 192.168.99.0 0.0.0.255 192.169.98.0 0.0.0.255",
        " permit ip 192.169.98.0 0.0.0.255 192.168.99.0 0.0.0.255",
        " permit ip 192.168.10.0 0.0.0.255 any",
        " permit ip 192.168.20.0 0.0.0.255 any",
        " permit ip 192.168.30.0 0.0.0.255 any",
        " permit ip 192.169.10.0 0.0.0.255 any",
        " permit ip 192.169.20.0 0.0.0.255 any",
        " permit ip 192.169.30.0 0.0.0.255 any",
        " permit ip 11.11.11.0 0.0.0.3 any",
        " permit ip 12.12.12.0 0.0.0.3 any",
        " permit ip 200.0.150.0 0.0.0.3 any",
        " permit ip 200.100.150.0 0.0.0.3 any",
        " deny ip any any",
        "ip access-list extended MGMT_ACCESS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " deny ip any any",
        "interface GigabitEthernet0/0",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "interface GigabitEthernet0/1",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "interface GigabitEthernet0/2",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "end",
        "write memory"
    ]
    configure_acl("ToISP_Router", "11.11.11.2", acl_commands)

def configure_acl_y_router():
    acl_commands = [
        "configure terminal",
        "ip access-list extended ALLOW_SPECIFIC_IPS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " permit ip 192.168.99.0 0.0.0.255 192.169.98.0 0.0.0.255",
        " permit ip 192.169.98.0 0.0.0.255 192.168.99.0 0.0.0.255",
        " permit ip 192.168.10.0 0.0.0.255 any",
        " permit ip 192.168.20.0 0.0.0.255 any",
        " permit ip 192.168.30.0 0.0.0.255 any",
        " permit ip 192.169.10.0 0.0.0.255 any",
        " permit ip 192.169.20.0 0.0.0.255 any",
        " permit ip 192.169.30.0 0.0.0.255 any",
        " permit ip 11.11.11.0 0.0.0.3 any",
        " permit ip 12.12.12.0 0.0.0.3 any",
        " permit ip 200.0.150.0 0.0.0.3 any",
        " permit ip 200.100.150.0 0.0.0.3 any",
        " deny ip any any",
        "ip access-list extended MGMT_ACCESS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " deny ip any any",
        "interface GigabitEthernet0/0",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "interface GigabitEthernet0/2",
        " ip access-group ALLOW_SPECIFIC_IPS in",
        "exit",
        "end",
        "write memory"
    ]
    configure_acl("Y_Router", "12.12.12.1", acl_commands)

def choose_router_and_configure_acl():
    print("Choose the router to configure ACLs:")
    print("1. GnB_Router")
    print("2. ToISP_Router")
    print("3. Y_Router")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        configure_acl_gnb_router()
    elif choice == '2':
        configure_acl_toisp_router()
    elif choice == '3':
        configure_acl_y_router()
    else:
        print("Invalid choice, returning to main menu.")

def manage_acl():
    logging.info("Starting ACL management...")
    choose_router_and_configure_acl()
    logging.info("ACL management completed.")

