import getpass
import sys

from netmiko import ConnectHandler

COMMAND = sys.argv[1]
USER = input('Username: ')
PASSWORD = getpass.getpass()

DEVICES_IP = ['192.168.32.1', '192.168.200.46']

for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))
    DEVICE_PARAMS = {
        'device_type': 'hp_procurve',
        'ip': IP,
        'username': USER,
        'password': PASSWORD
    }

    with ConnectHandler(**DEVICE_PARAMS) as ssh:
        ssh.enable()
	ssh.send_command("1")
        result = ssh.send_command(COMMAND)
        print(result)
