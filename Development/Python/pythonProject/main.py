from logging import exception

import paramiko
ips = ['172.16.0.104', '172.16.3.156', '172.16.3.185', '172.16.3.187', '172.16.3.203', '192.168.225.4',
      '192.168.225.5', '192.168.225.7', '192.168.225.9', '192.168.225.10', '192.168.225.11', '192.168.225.12',
      '192.168.225.14', '192.168.225.15', '192.168.225.17', '192.168.225.18', '192.168.225.19', '192.168.225.20',
      '192.168.225.21', '192.168.225.22', '192.168.225.23', '192.168.225.24', '192.168.225.25', '192.168.225.26',
      '192.168.225.27', '192.168.225.29', '192.168.225.30', '192.168.225.33', '192.168.225.35', '192.168.225.38']

for ip in ips:
    host = ip
    port = 22
    username = "aditya.verma"
    password = "@dity@0913"
    command = "ls"
    print("Connecting to "+ip)
    try :
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials: %s")
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
    except paramiko.BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
    finally:
        ssh.close()


