import paramiko
import logging

class SSHConnection:
    def __init__(self, hostname, username, key_file):
        self.hostname = hostname
        self.username = username
        self.key_file = key_file
        self.client = None
        self.shell = None

    def establish_ssh_connection(self):
        try:
            logging.info(f"Establishing SSH connection to {self.hostname}.")
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(
                hostname=self.hostname,
                username=self.username,
                key_filename=self.key_file,
                look_for_keys=False,
                allow_agent=False
            )
            self.shell = self.client.invoke_shell()
            logging.info(f"SSH connection established to {self.hostname}.")
            self.wait_for_prompt()
        except Exception as e:
            logging.error(f"Failed to establish SSH connection to {self.hostname}: {e}")
            if self.client:
                self.client.close()
            raise

    def wait_for_prompt(self):
        while not self.shell.recv_ready():
            pass
        output = self.shell.recv(5000).decode('utf-8')
        logging.info(f"SSH prompt received: {output.strip()}")

    def execute_commands(self, commands):
        try:
            for command in commands:
                logging.info(f"Sending command: {command}")
                self.shell.send(command + '\n')
                self.wait_for_prompt()
                output = self.shell.recv(5000).decode('utf-8')
                logging.info(f"Command output: {output.strip()}")
        except Exception as e:
            logging.error(f"An error occurred while executing commands: {e}")
            raise

    def close_connection(self):
        if self.client:
            logging.info("Closing SSH connection.")
            self.client.close()
