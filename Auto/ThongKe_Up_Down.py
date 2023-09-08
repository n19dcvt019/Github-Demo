from netmiko import ConnectHandler
import pandas as pd

R = {
    'device_type':'cisco_ios',
    'ip':'192.168.47.100',
    'username':'admin',
    'password':'123',
    'secret':'vnpro',
}

net_connect = ConnectHandler(**R)
net_connect.enable()

output = net_connect.send_command('sh ip int bri')

lines = output.split('\n')  #tách từng dòng thành văn bản

results = []
headers = lines[0].split()  #tách dòng tiêu đề thành các cột

for line in lines[1:]:
    if 'down' in headers:
        data = line.split()       #tách dữ liệu thành cột
        results.append(data)
df = pd.DataFrame(results, columns = headers)
#print(df)

#Lưu DataFrame vào file Excel
df.to_excel("ketqua.xlsx", index=False)
