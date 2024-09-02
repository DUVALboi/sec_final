import logging
from ssh_connection import SSHConnection

def configure_firewall(router_name, router_ip, commands):
    try:
        logging.info(f"Configuring firewall on {router_name} ({router_ip})...")
        ssh_conn = SSHConnection(router_ip, 'admin1', 'ssh/id_rsa')
        ssh_conn.establish_ssh_connection()
        ssh_conn.execute_commands(commands)
        ssh_conn.close_connection()
        logging.info(f"Firewall configuration applied to {router_name} ({router_ip}).")
    except Exception as e:
        logging.error(f"An error occurred while configuring {router_name}: {e}")

def configure_firewall_gnb_router():
    commands = [
        "configure terminal",
        "ip access-list extended FIREWALL_INBOUND",
        " permit ip any any",
        " exit",
        "ip access-list extended FIREWALL_OUTBOUND",
        " permit ip any any",
        " exit",
        "interface GigabitEthernet0/1",
        " ip access-group FIREWALL_INBOUND in",
        " ip access-group FIREWALL_OUTBOUND out",
        " exit",
        "interface GigabitEthernet0/6",
        " ip access-group FIREWALL_INBOUND in",
        " exit",
        "interface GigabitEthernet0/7",
        " ip access-group FIREWALL_INBOUND in",
        " exit",
        "end",
        "write memory"
    ]
    configure_firewall("GnB_Router", "11.11.11.1", commands)

def configure_firewall_toisp_router():
    commands = [
        "configure terminal",
        "ip access-list extended FIREWALL_INBOUND",
        " permit ip any any",
        " exit",
        "ip access-list extended FIREWALL_OUTBOUND",
        " permit ip any any",
        " exit",
        "interface GigabitEthernet0/0",  # Interface leading to NAT
        " ip access-group FIREWALL_INBOUND in",
        " ip access-group FIREWALL_OUTBOUND out",
        " exit",
        "interface GigabitEthernet0/1",
        " ip access-group FIREWALL_INBOUND in",
        " ip access-group FIREWALL_OUTBOUND out",
        " exit",
        "interface GigabitEthernet0/2",
        " ip access-group FIREWALL_INBOUND in",
        " exit",
        "end",
        "write memory"
    ]
    configure_firewall("ToISP_Router", "11.11.11.2", commands)

def configure_firewall_y_router():
    commands = [
        "configure terminal",
        "ip access-list extended FIREWALL_INBOUND",
        " permit ip any any",
        " exit",
        "ip access-list extended FIREWALL_OUTBOUND",
        " permit ip any any",
        " exit",
        "interface GigabitEthernet0/2",  # Interface connecting to ToISP
        " ip access-group FIREWALL_INBOUND in",
        " ip access-group FIREWALL_OUTBOUND out",
        " exit",
        "interface GigabitEthernet0/0",  # Interface leading to the yellow zone
        " ip access-group FIREWALL_INBOUND in",
        " exit",
        "end",
        "write memory"
    ]
    configure_firewall("Y_Router", "12.12.12.1", commands)

def choose_router_and_configure_firewall():
    print("Choose the router to configure firewall:")
    print("1. GnB_Router")
    print("2. ToISP_Router")
    print("3. Y_Router")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        configure_firewall_gnb_router()
    elif choice == '2':
        configure_firewall_toisp_router()
    elif choice == '3':
        configure_firewall_y_router()
    else:
        print("Invalid choice, returning to main menu.")

def manage_firewall():
    logging.info("Starting firewall management...")
    choose_router_and_configure_firewall()
    logging.info("Firewall management completed.")
