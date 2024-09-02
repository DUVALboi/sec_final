import logging
from ssh_connection import SSHConnection

def configure_aaa(router_name, router_ip, commands):
    try:
        logging.info(f"Configuring AAA on {router_name} ({router_ip})...")
        ssh_conn = SSHConnection(router_ip, 'admin1', 'ssh/id_rsa')
        ssh_conn.establish_ssh_connection()
        ssh_conn.execute_commands(commands)
        ssh_conn.close_connection()
        logging.info(f"AAA configuration applied to {router_name} ({router_ip}).")
    except Exception as e:
        logging.error(f"An error occurred while configuring {router_name}: {e}")

def configure_aaa_gnb_router():
    commands = [
        "configure terminal",
        "aaa new-model",
        "aaa group server radius RAD-SERVER",
        "server 192.168.40.50 auth-port 1812 acct-port 1813 key YOUR_SHARED_SECRET",
        "aaa authentication login default group RAD-SERVER local",
        "aaa authorization exec default group RAD-SERVER local",
        "aaa authorization commands 15 default group RAD-SERVER local",
        "aaa accounting exec default start-stop group RAD-SERVER",
        "aaa accounting commands 15 default start-stop group RAD-SERVER",
        "ip access-list extended MGMT_ACCESS",
        "permit ip host 192.168.40.40 any",
        "permit ip host 192.169.30.30 any",
        "deny ip any any",
        "line vty 0 4",
        "access-class MGMT_ACCESS in",
        "login authentication default",
        "end",
        "write memory"
    ]
    configure_aaa("GnB_Router", "11.11.11.1", commands)

def configure_aaa_toisp_router():
    commands = [
        "configure terminal",
        "aaa new-model",
        "aaa group server radius RAD-SERVER",
        "server 192.168.40.50 auth-port 1812 acct-port 1813 key YOUR_SHARED_SECRET",
        "aaa authentication login default group RAD-SERVER local",
        "aaa authorization exec default group RAD-SERVER local",
        "aaa authorization commands 15 default group RAD-SERVER local",
        "aaa accounting exec default start-stop group RAD-SERVER",
        "aaa accounting commands 15 default start-stop group RAD-SERVER",
        "ip access-list extended MGMT_ACCESS",
        "permit ip host 192.168.40.40 any",
        "permit ip host 192.169.30.30 any",
        "deny ip any any",
        "line vty 0 4",
        "access-class MGMT_ACCESS in",
        "login authentication default",
        "end",
        "write memory"
    ]
    configure_aaa("ToISP_Router", "11.11.11.2", commands)

def configure_aaa_y_router():
    commands = [
        "configure terminal",
        "aaa new-model",
        "aaa group server radius RAD-SERVER",
        "server 192.168.40.50 auth-port 1812 acct-port 1813 key YOUR_SHARED_SECRET",
        "aaa authentication login default group RAD-SERVER local",
        "aaa authorization exec default group RAD-SERVER local",
        "aaa authorization commands 15 default group RAD-SERVER local",
        "aaa accounting exec default start-stop group RAD-SERVER",
        "aaa accounting commands 15 default start-stop group RAD-SERVER",
        "ip access-list extended MGMT_ACCESS",
        "permit ip host 192.168.40.40 any",
        "permit ip host 192.169.30.30 any",
        "deny ip any any",
        "line vty 0 4",
        "access-class MGMT_ACCESS in",
        "login authentication default",
        "end",
        "write memory"
    ]
    configure_aaa("Y_Router", "12.12.12.1", commands)

def choose_router_and_configure_aaa():
    print("Choose the router to configure AAA:")
    print("1. GnB_Router")
    print("2. ToISP_Router")
    print("3. Y_Router")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        configure_aaa_gnb_router()
    elif choice == '2':
        configure_aaa_toisp_router()
    elif choice == '3':
        configure_aaa_y_router()
    else:
        print("Invalid choice, returning to main menu.")

def manage_aaa():
    logging.info("Starting AAA management...")
    choose_router_and_configure_aaa()
    logging.info("AAA management completed.")
