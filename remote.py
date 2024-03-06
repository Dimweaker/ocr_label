from paramiko import SSHClient, AutoAddPolicy
from pandas import read_csv
from io import StringIO

class Remote:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())

    def connect(self):
        self.client.connect(self.host, username=self.user, password=self.password)

    def close(self):
        self.client.close()

    def load_data(self, remote_path, buffer_path):
        self.connect()
        ftp_client = self.client.open_sftp()
        ftp_client.get(remote_path, buffer_path)
        ftp_client.close()
        self.close()

    def save_data(self, buffer_path, remote_path):
        self.connect()
        ftp_client = self.client.open_sftp()
        ftp_client.put(buffer_path, remote_path)
        ftp_client.close()
        self.close()