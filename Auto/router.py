from netmiko import ConnectHandler

R = {
    'device_type':'cisco_ios',
    'ip':'192.168.47.100',
    'username':'admin',
    'password':'123',
    'secret':'vnpro',
}

net_connect = ConnectHandler(**R)
net_connect.enable()

status = ['int e0/1', 'no shutdown']
output = net_connect.send_config_set(status)

output = net_connect.send_command('show ip int bri')

print(output)
'''dem = 0
for line in output.splitlines():
    if "Interface" in line:
        continue
    elif "down" in line:
        dem += 1

print("So interface down cua thiet bi la: ", dem)'''
