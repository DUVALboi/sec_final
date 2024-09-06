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

def generate_aaa_commands():
    return [
        "configure terminal",
        "aaa new-model",
        "aaa group server radius RAD-SERVER",
        " server 192.168.40.50 auth-port 1812 acct-port 1813",
        " key YOUR_SHARED_SECRET",
        "aaa authentication login default group RAD-SERVER local",
        "aaa authorization exec default group RAD-SERVER local",
        "aaa authorization commands 15 default group RAD-SERVER local",
        "aaa accounting exec default start-stop group RAD-SERVER",
        "aaa accounting commands 15 default start-stop group RAD-SERVER",
        "ip access-list extended MGMT_ACCESS",
        " permit ip host 192.168.40.40 any",
        " permit ip host 192.169.30.30 any",
        " deny ip any any",
        "line vty 0 4",
        " access-class MGMT_ACCESS in",
        " login authentication default",
        "end",
        "write memory"
    ]

def configure_aaa_router(router_name, router_ip):
    commands = generate_aaa_commands()
    configure_aaa(router_name, router_ip, commands)

def choose_router_and_configure_aaa():
    router_options = {
        '1': ("GnB_Router", "11.11.11.1"),
        '2': ("ToISP_Router", "11.11.11.2"),
        '3': ("Y_Router", "12.12.12.1")
    }
    
    print("Choose the router to configure AAA:")
    for key, (name, _) in router_options.items():
        print(f"{key}. {name}")
    
    choice = input("Enter your choice: ")

    if choice in router_options:
        router_name, router_ip = router_options[choice]
        configure_aaa_router(router_name, router_ip)
    else:
        print("Invalid choice, returning to main menu.")

def manage_aaa():
    logging.info("Starting AAA management...")
    choose_router_and_configure_aaa()
    logging.info("AAA management completed.")
