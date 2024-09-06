import paramiko
import logging
import time

class SSHConnection:
    def __init__(self, router_ip, username, key_file):
        self.router_ip = router_ip
        self.username = username
        self.key_file = key_file
        self.client = None
        self.shell = None

    def establish_ssh_connection(self):
        try:
            # Setting up SSH client with RSA private key authentication
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            private_key = paramiko.RSAKey.from_private_key_file(self.key_file)

            logging.info(f"Establishing SSH connection to {self.router_ip}...")
            self.client.connect(self.router_ip, username=self.username, pkey=private_key)
            logging.info(f"SSH connection established to {self.router_ip}.")
            
            # Open shell session for continuous commands
            self.shell = self.client.invoke_shell()
            logging.info("Shell session opened.")
            time.sleep(1)  # Giving time for shell to initialize
            self._flush_shell_output()  # Clean any previous outputs

        except Exception as e:
            logging.error(f"Failed to establish SSH connection: {e}")
            if self.client:
                self.client.close()

    def execute_commands(self, commands):
        try:
            for command in commands:
                logging.info(f"Sending command: {command}")
                self.shell.send(command + '\n')
                time.sleep(1)  # Give command some time to execute
                output = self._receive_shell_output()
                logging.info(f"Command output: {output}")
        except Exception as e:
            logging.error(f"An error occurred while executing commands: {e}")

    def execute_command(self, command):
        # Same as execute_commands but for a single command
        try:
            logging.info(f"Sending command: {command}")
            self.shell.send(command + '\n')
            time.sleep(1)
            output = self._receive_shell_output()
            logging.info(f"Command output: {output}")
        except Exception as e:
            logging.error(f"An error occurred while executing command: {e}")

    def _flush_shell_output(self):
        if self.shell.recv_ready():
            return self.shell.recv(65535).decode('utf-8')

    def _receive_shell_output(self):
        output = ""
        while not self.shell.recv_ready():
            time.sleep(0.1)  # Small wait to reduce CPU usage
        while self.shell.recv_ready():
            output += self.shell.recv(65535).decode('utf-8')
        return output.strip()

    def close_connection(self):
        try:
            if self.client:
                logging.info("Closing SSH connection.")
                self.client.close()
                logging.info("SSH connection closed.")
        except Exception as e:
            logging.error(f"An error occurred while closing the connection: {e}")

