import logging
import socket

def listen_on_nat_interface(nat_ip, nat_port=80):
    try:
        logging.info(f"Listening on NAT interface {nat_ip}:{nat_port}...")

        # Create a raw socket to listen to all traffic on the specified NAT interface
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.bind((nat_ip, nat_port))

        logging.info(f"Listening for traffic on {nat_ip}:{nat_port}")

        while True:
            packet, addr = sock.recvfrom(65535)
            logging.info(f"Packet received from {addr}: {packet}")

    except KeyboardInterrupt:
        logging.info("Stopping the NAT interface listener.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        sock.close()
        logging.info("Socket closed.")

def manage_listen():
    logging.info("Starting NAT listening management...")
    nat_ip = input("Enter the NAT interface IP to listen on: ")
    nat_port = int(input("Enter the NAT interface port to listen on (default 80): ") or 80)
    listen_on_nat_interface(nat_ip, nat_port)
    logging.info("NAT listening management completed.")
