import logging
import time
from ssh_connection import SSHConnection

def start_packet_capture(router_ip, router_username, key_file):
    commands = [
        "monitor capture buffer CAPTURE_BUFFER size 10000 circular",
        "monitor capture point ip cef CAPTURE_POINT g0/0 both",
        "monitor capture point associate CAPTURE_POINT CAPTURE_BUFFER",
        "monitor capture point start CAPTURE_POINT"
    ]
    
    try:
        # Establish SSH connection
        logging.info(f"Establishing SSH connection to {router_ip}...")
        ssh_conn = SSHConnection(router_ip, router_username, key_file)
        ssh_conn.establish_ssh_connection()

        # Execute the capture commands
        logging.info(f"Starting packet capture on {router_ip} (g0/0)...")
        ssh_conn.execute_commands(commands)
        logging.info(f"Packet capture started on {router_ip} (g0/0).")

        # Keep capturing and displaying the packets using show command
        logging.info(f"Packet capture active on {router_ip}... Press Ctrl+C to stop.")
        while True:
            # Using show monitor capture to display captured packets
            show_command = ["show monitor capture buffer CAPTURE_BUFFER"]
            ssh_conn.execute_commands(show_command)
            time.sleep(5)  # Sleep for a few seconds before fetching the next capture

    except KeyboardInterrupt:
        logging.info("Stopping the packet capture manually...")
        ssh_conn.execute_commands([
            "monitor capture point stop CAPTURE_POINT"
        ])
    except Exception as e:
        logging.error(f"An error occurred while capturing packets on {router_ip}: {e}")
    finally:
        # Stop the capture and clear the buffer
        stop_capture_commands = [
            "monitor capture point stop CAPTURE_POINT",
            "monitor capture buffer CAPTURE_BUFFER clear"
        ]
        ssh_conn.execute_commands(stop_capture_commands)

        # Close the SSH connection
        ssh_conn.close_connection()
        logging.info("SSH connection closed.")

def manage_listen():
    logging.info("Starting NAT listening management...")
    router_ip = input("Enter the ToISP router IP: ")
    router_username = input("Enter the router username: ")
    key_file = input("Enter the SSH private key file path: ")
    start_packet_capture(router_ip, router_username, key_file)
    logging.info("NAT listening management completed.")

