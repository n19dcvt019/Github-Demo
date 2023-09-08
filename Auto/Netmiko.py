from netmiko import ConnectHandler
SW = {
    'device_type':'cisco_ios',
    'ip':'192.168.47.228',
    'username':'admin',
    'password':'123',
    'secret':'vnpro',
}

net_connect = ConnectHandler(**SW)
net_connect.enable()

for n in range (10,21):
    taoVlan= ['vlan' + str(n)]

    ipVlan = ['int vlan ' + str(n), 'ip address 172.16.' + str(n) + '.1 255.255.255.0' , 'no shutdown']
    output = net_connect.send_config_set(taoVlan)
    output = net_connect.send_config_set(ipVlan)
output = net_connect.send_command('sh ip int bri | i Vlan')
print(output)


for n in range (10,21):
    xoaVlan = ['no int vlan' + str(n)]
    output = net_connect.send_config_set(xoaVlan)

output = net_connect.send_command('sh ip int bri | i Vlan')
print(output)
