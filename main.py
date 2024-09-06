import os
import logging
from acl_management import manage_acl
from firewall_management import manage_firewall
from management_aaa import manage_aaa
from listen import manage_listen

from logs import setup_logging

LOG_FILE_PATH = 'logs/security_automation.log'

def main():
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)
        print(f"Deleted {LOG_FILE_PATH}.")

    setup_logging()
    logging.info("Program started.")

    while True:
        print("1. Manage ACLs")
        print("2. Manage Firewall")
        print("3. Manage AAA")
        print("4. Listen to NAT Traffic")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_acl()
        elif choice == '2':
            manage_firewall()
        elif choice == '3':
            manage_aaa()
        elif choice == '4':
            manage_listen()
        elif choice == '5':
            logging.info("Program exited by user.")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
