from router_connect import interface

try:
    assert interface[0] == 'ssh admin:cisco@192.168.1.1 -p 2231'
    print('Passed')
except AssertionError:
    print('Failed')
try:
    assert interface[1] == 'ssh admin:microtik@192.168.2.1 -p 2213'
    print('Passed')
except AssertionError:
    print('Failed')