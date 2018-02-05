from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time

import yaml
from netmiko import ConnectHandler

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command='sh clock'):
    print(start_msg.format(datetime.now().time(), device_dict['ip']))
    if device_dict['ip'] == '192.168.100.1':
        time.sleep(10)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print(received_msg.format(datetime.now().time(), device_dict['ip']))
    return {device_dict['ip']: result}


def threads_conn(function, devices, limit=2):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, devices)
    return list(f_result)


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = threads_conn(connect_ssh, devices['routers'])
    pprint(all_done)
