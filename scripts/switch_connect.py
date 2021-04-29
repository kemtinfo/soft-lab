import yaml

with open(r'../switches.yaml', 'r') as in_file:
    devices = yaml.safe_load(in_file)

def get_connect(dev: dict, ssh=[]):
    for item in dev:
        device = dev[item]
        connect = f"ssh {device['user']['name']}:{device['user']['password']}@{device['mgmt_ip']} -p {device['port']}"
        ssh.append(connect)
    return ssh

interface = get_connect(devices)