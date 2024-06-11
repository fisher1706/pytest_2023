import pytest
# import yaml
from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException


@pytest.fixture
def topology_with_dupl_links():
    topology = {
        ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')
    }
    return topology


@pytest.fixture
def normalized_topology_example():
    normalized_topology = {
        ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
        ('R3', 'Eth0/2'): ('R5', 'Eth0/0')
    }
    return normalized_topology


# @pytest.fixture(scope='module')
# def first_router_from_devices_yaml():
#     with open('devices.yaml') as f:
#         devices = yaml.safe_load(f)
#         r1 = devices[0]
#     return r1


@pytest.fixture(scope='module')
def first_router_wrong_pass(first_router_from_devices_yaml):
    r1 = first_router_from_devices_yaml.copy()
    r1['password'] = 'wrong'
    return r1


def first_router_wrong_ip(first_router_from_devices_yaml):
    r1 = first_router_from_devices_yaml.copy()
    r1['ip'] = 'unreachable'
    return r1


def r1_test_connection(first_router_from_devices_yaml):
    with ConnectHandler(**first_router_from_devices_yaml) as r1:
        r1.enable()
    yield r1


@pytest.fixture()
def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except AuthenticationException as error:
        print(error)


@pytest.fixture(params=[1, 2, 3])
def param_fixture(request):
    return request.param


@pytest.fixture(params=["apple", "banana", "cherry"])
def fruit_fixture(request):
    return request.param


@pytest.fixture(params=[100, 200, 300])
def number_fixture(request):
    return request.param
